param(
    [string]$Root = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$rootPath = [System.IO.Path]::GetFullPath($Root)
$lockPath = Join-Path $rootPath "BASELINE_LOCK.json"

if (-not (Test-Path -LiteralPath $lockPath)) {
    throw "Missing BASELINE_LOCK.json at $lockPath"
}

$lock = Get-Content -Raw -LiteralPath $lockPath | ConvertFrom-Json
$failures = New-Object System.Collections.Generic.List[string]

foreach ($repo in $lock.source_repositories) {
    $modulePath = Join-Path $rootPath $repo.path
    if (-not (Test-Path -LiteralPath $modulePath)) {
        $failures.Add("Missing submodule path: $($repo.path)")
        continue
    }

    $head = (& git -C $modulePath rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("Cannot read HEAD for $($repo.path)")
        continue
    }

    if ($head -ne $repo.commit) {
        $failures.Add("HEAD mismatch for $($repo.path): expected $($repo.commit), got $head")
    }

    $dirty = (& git -C $modulePath status --porcelain=v1 -uall)
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("Cannot read status for $($repo.path)")
        continue
    }

    if ($dirty) {
        $failures.Add("Dirty submodule: $($repo.path)")
    }
}

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Output "[FAIL] $_" }
    exit 1
}

Write-Output "[OK] Submodule pins match BASELINE_LOCK.json and submodules are clean."
