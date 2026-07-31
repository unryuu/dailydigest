# monitor_crash.ps1 — Claude Desktop 闪退取证监控
#
# 起因：2026-07-30/31 客户端反复闪退，但三种痕迹一个都不留（无 Application Error、
# 无 Crashpad 转储、无内核事件），无法判断是「进程真死」还是「只是界面重载」。
# 本脚本独立于客户端运行，客户端死了它照跑。
#
# 用法（新开一个 PowerShell 窗口，普通权限即可）：
#     powershell -ExecutionPolicy Bypass -NoExit -File E:\dailydigest\scripts\monitor_crash.ps1
# 停止：在该窗口按 Ctrl+C
#
# 产物（reports\_debug\）：
#   monitor-<日期>.csv          每 15 秒一行：进程 PID、启动时间、内存、系统空闲内存
#   events-<日期>.log           只记异常：进程消失/新增、日志被清空、WerFault 出现、新崩溃转储
#   mainlog-<日期>.txt          持续把客户端 main.log 的新内容抄下来，客户端重启清空也不丢

param(
    [int]$IntervalSeconds = 15,
    [string]$OutDir = "E:\dailydigest\reports\_debug"
)

$ErrorActionPreference = 'Continue'
$stamp    = Get-Date -Format 'yyyyMMdd'
$csvPath  = Join-Path $OutDir "monitor-$stamp.csv"
$evtPath  = Join-Path $OutDir "events-$stamp.log"
$logPath  = Join-Path $OutDir "mainlog-$stamp.txt"
$appLog   = "$env:APPDATA\Claude\logs\main.log"
$crashDir = "$env:APPDATA\Claude\Crashpad\reports"

if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir -Force | Out-Null }
if (-not (Test-Path $csvPath)) {
    'Time,PidCount,Pids,TotalWS_MB,SysFreeMB,MainLogLen,WerFault' | Out-File $csvPath -Encoding utf8
}

function Write-Event([string]$msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
    Add-Content -Path $evtPath -Value $line -Encoding utf8
    Write-Host $line -ForegroundColor Yellow
}

# 从指定偏移量读取被占用的文件（客户端一直开着 main.log，必须共享读写）
function Read-From([string]$path, [long]$offset) {
    $share = [System.IO.FileShare]::ReadWrite -bor [System.IO.FileShare]::Delete
    $fs = New-Object System.IO.FileStream -ArgumentList $path, ([System.IO.FileMode]::Open), ([System.IO.FileAccess]::Read), $share
    try {
        $len = $fs.Length
        $truncated = $false
        if ($offset -gt $len) { $offset = 0; $truncated = $true }
        $count = $len - $offset
        $text = ''
        if ($count -gt 0) {
            $fs.Seek($offset, [System.IO.SeekOrigin]::Begin) | Out-Null
            $buf = New-Object byte[] $count
            $read = $fs.Read($buf, 0, $count)
            $text = [System.Text.Encoding]::UTF8.GetString($buf, 0, $read)
        }
        return @{ Text = $text; Length = $len; Truncated = $truncated }
    } finally { $fs.Dispose() }
}

$knownPids   = @{}      # pid -> 启动时间
$logOffset   = 0
$knownCrash  = @{}
$firstTick   = $true

Write-Event "=== 监控启动，间隔 ${IntervalSeconds}s，产物目录 $OutDir ==="
Write-Event "客户端日志路径 = $appLog"
Write-Event "Test-Path = $(Test-Path $appLog) / .NET Exists = $([System.IO.File]::Exists($appLog))"
Write-Event "本进程已提权 = $(([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))  用户 = $env:USERNAME"
Write-Host "运行中。客户端崩了不要关这个窗口。停止按 Ctrl+C。`n" -ForegroundColor Cyan

while ($true) {
    try {
        $now = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
        $procs = @(Get-Process -Name claude -ErrorAction SilentlyContinue)
        $curr = @{}
        $totalWS = 0
        foreach ($p in $procs) {
            $st = ''
            try { $st = $p.StartTime.ToString('HH:mm:ss') } catch { $st = '?' }
            $curr[$p.Id] = $st
            $totalWS += $p.WorkingSet64
        }

        # 进程增减
        if (-not $firstTick) {
            foreach ($k in $knownPids.Keys) {
                if (-not $curr.ContainsKey($k)) { Write-Event "进程消失  PID=$k (启动于 $($knownPids[$k]))" }
            }
            foreach ($k in $curr.Keys) {
                if (-not $knownPids.ContainsKey($k)) { Write-Event "进程新增  PID=$k (启动于 $($curr[$k]))" }
            }
        } else {
            Write-Event "初始快照  claude 进程 $($curr.Count) 个：$(($curr.Keys | Sort-Object) -join ' ')"
        }
        $knownPids = $curr

        # WerFault 出现 = Windows 正在处理某个崩溃
        $wer = @(Get-Process -Name WerFault, WerFaultSecure -ErrorAction SilentlyContinue)
        $werIds = ($wer | ForEach-Object { $_.Id }) -join ' '
        if ($wer.Count -gt 0) { Write-Event "WerFault 出现  PID=$werIds  <<< Windows 正在记录一个崩溃" }

        # 新的 Crashpad 转储
        if (Test-Path $crashDir) {
            foreach ($f in @(Get-ChildItem $crashDir -File -ErrorAction SilentlyContinue)) {
                if (-not $knownCrash.ContainsKey($f.Name)) {
                    $knownCrash[$f.Name] = 1
                    if (-not $firstTick) { Write-Event "新崩溃转储  $($f.Name)  $([int]($f.Length/1KB))KB  <<< 抓到了" }
                }
            }
        }

        # 抄 main.log 的新内容，被清空说明客户端重启了
        # 单独包一层：这里出错只记原因，不连累整拍的记录
        # 不用 Test-Path 试探（提权进程上出现过明明存在却报 False），直接开文件，
        # 开不了就把真实异常记下来。恢复了会自动接着抄。
        $logLen = -1
        try {
            $r = Read-From $appLog $logOffset
            $logLen = $r.Length
            if ($r.Truncated) { Write-Event "main.log 被清空  <<< 客户端重启了" }
            if ($r.Text.Length -gt 0) { Add-Content -Path $logPath -Value $r.Text -Encoding utf8 -NoNewline }
            $logOffset = $r.Length
            if ($script:logBroken) {
                Write-Event "抄日志已恢复，当前 $logLen 字节"
                $script:logBroken = $false
            }
        } catch {
            $logLen = -3
            if (-not $script:logBroken) {
                Write-Event "抄日志失败：$($_.Exception.GetType().Name) - $($_.Exception.Message)"
                $script:logBroken = $true
            }
        }

        $free = [int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1KB)
        $row = '{0},{1},{2},{3},{4},{5},{6}' -f $now, $curr.Count,
               (($curr.Keys | Sort-Object) -join ' '), [int]($totalWS / 1MB), $free, $logLen, $werIds
        Add-Content -Path $csvPath -Value $row -Encoding utf8

        if ($firstTick -or ((Get-Date).Second -lt $IntervalSeconds)) {
            Write-Host "$now  进程 $($curr.Count) 个  占用 $([int]($totalWS/1MB))MB  系统空闲 ${free}MB"
        }
        $firstTick = $false
    } catch {
        Write-Event "监控自身异常（已忽略继续跑）：$_"
    }
    Start-Sleep -Seconds $IntervalSeconds
}
