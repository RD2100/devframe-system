param(
    [string]$Root = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$rootPath = [System.IO.Path]::GetFullPath($Root)

$requiredPaths = @(
    "AGENTS.md",
    "rules",
    "schemas",
    "docs\agent-runtime",
    "templates\runtime-bootstrap",
    "BASELINE_LOCK.json",
    "BOOTSTRAP_REPORT.md",
    "COMPLETION_MATRIX.md",
    "PAPER_FEATURE_STATUS.md",
    "INTEGRATION_STATUS.md",
    "SUBMODULES.md",
    "RISK_REGISTER.md",
    "RUNBOOK.md",
    "integration\lock\submodules.lock.yml",
    "integration\plans\minimal_dag_v2_1.md",
    "integration\contracts\README.md",
    "integration\contracts\evidence-zip-review.md",
    "integration\reports\README.md",
    "integration\runbooks\gitlab-ci-readonly-policy.md",
    "integration\paper\README.md",
    "integration\task-specs\README.md",
    "integration\task-specs\TS-AGENT-ACCEPTANCE-PATH-GATE0.md",
    "integration\task-specs\TS-CONTROL-PLANE-LEASE-LOCK.md",
    "integration\task-specs\TS-OPENCODE-RUNTIME-AUTH.md",
    "integration\task-specs\TS-PAPER-FEATURE-FOCUS.md",
    "integration\task-specs\TS-TEST-FRAME-ADAPTER.md",
    ".gitlab-ci.yml",
    "scripts\check-submodules.ps1",
    "scripts\readonly-inventory.ps1",
    "scripts\review_a120_evidence_zip.py"
)

$missing = New-Object System.Collections.Generic.List[string]

foreach ($path in $requiredPaths) {
    $fullPath = Join-Path $rootPath $path
    if (-not (Test-Path -LiteralPath $fullPath)) {
        $missing.Add($path)
    }
}

if ($missing.Count -gt 0) {
    $missing | ForEach-Object { Write-Output "[MISSING] $_" }
    exit 1
}

$jsonFailures = New-Object System.Collections.Generic.List[string]
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$jsonRoots = @(
    "schemas",
    "integration"
)

foreach ($jsonRoot in $jsonRoots) {
    $jsonRootPath = Join-Path $rootPath $jsonRoot
    if (-not (Test-Path -LiteralPath $jsonRootPath)) {
        continue
    }

    Get-ChildItem -LiteralPath $jsonRootPath -Recurse -Filter "*.json" | ForEach-Object {
        try {
            $jsonText = [System.IO.File]::ReadAllText($_.FullName, $utf8)
            if ($jsonText.Length -gt 0 -and $jsonText[0] -eq [char]0xFEFF) {
                $jsonText = $jsonText.Substring(1)
            }
            $jsonText | ConvertFrom-Json | Out-Null
        } catch {
            $relativePath = [System.IO.Path]::GetRelativePath($rootPath, $_.FullName)
            $jsonFailures.Add("${relativePath}: $($_.Exception.Message)")
        }
    }
}

if ($jsonFailures.Count -gt 0) {
    $jsonFailures | ForEach-Object { Write-Output "[JSON-FAIL] $_" }
    exit 1
}

Write-Output "[OK] Required Phase 0.5 inventory files are present."
Write-Output "[OK] JSON inventory files parse as UTF-8."
Write-Output "[INFO] This script is read-only and does not run project runtime or tests."
