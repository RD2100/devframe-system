<#
.SYNOPSIS
    Bootstrap the RD2100 Agent Runtime governance framework in any project.
.DESCRIPTION
    Copies universal assets (rules, schemas, reviewer docs) and generates
    project-specific files from templates.
.PARAMETER ProjectName
    Auto-detected from directory or git remote if omitted.
.PARAMETER ProjectRoot
    Defaults to current directory.
.PARAMETER Platform
    Claude, Codex, or Both. Default: Both.
.PARAMETER Phase
    Phase designation. Default: 0-5.
.PARAMETER DryRun
    Preview without writing files.
.PARAMETER Force
    Overwrite existing files.
.EXAMPLE
    .\bootstrap.ps1
    .\bootstrap.ps1 -ProjectName "my-app" -ProjectRoot "D:\my-app" -DryRun
#>

param(
    [string]$ProjectName = "",
    [string]$ProjectRoot = "",
    [string]$Platform = "Both",
    [string]$Phase = "0-5",
    [switch]$DryRun,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$TemplateDir = $ScriptDir

if (-not $ProjectRoot) { $ProjectRoot = Get-Location | Select-Object -ExpandProperty Path }
$ProjectRoot = [System.IO.Path]::GetFullPath($ProjectRoot)

if (-not (Test-Path $ProjectRoot)) {
    if ($DryRun) { Write-Output "[DRY-RUN] Would create: $ProjectRoot" }
    else { New-Item -ItemType Directory -Force -Path $ProjectRoot | Out-Null; Write-Output "[INFO] Created: $ProjectRoot" }
}

if (-not $ProjectName) {
    $ProjectName = Split-Path $ProjectRoot -Leaf
    try { $gitRemote = git -C $ProjectRoot remote get-url origin 2>$null; if ($gitRemote -match '([^/]+?)(\.git)?$') { $ProjectName = $Matches[1] } } catch { }; $global:LASTEXITCODE = 0
}

$GitRemote = "N/A"; try { $GitRemote = git -C $ProjectRoot remote get-url origin 2>$null; if (-not $GitRemote) { $GitRemote = "N/A" } } catch { }; $global:LASTEXITCODE = 0
$CurrentDate = Get-Date -Format "yyyy-MM-dd"

Write-Output "[INFO] Project: $ProjectName | Root: $ProjectRoot | Platform: $Platform | Phase: $Phase"

$Placeholders = @{
    "{{PROJECT_NAME}}" = $ProjectName; "{{PROJECT_ROOT}}" = $ProjectRoot
    "{{CURRENT_DATE}}" = $CurrentDate; "{{GIT_REMOTE}}" = $GitRemote
    "{{PHASE}}" = $Phase; "{{PLATFORM}}" = $Platform
}
# Governance manifest placeholders filled after GEN step
$ManifestPlaceholders = @{}

$SourceRoot = "D:\agent-acceptance"
if (-not (Test-Path $SourceRoot)) { Write-Error "Source not found: $SourceRoot"; exit 1 }

function Copy-Universal($srcRel, $dstRel, $desc) {
    $src = Join-Path $SourceRoot $srcRel; $dst = Join-Path $ProjectRoot $dstRel
    if ($DryRun) { Write-Output "[DRY-RUN] Copy: $srcRel -> $dstRel ($desc)"; return }
    if (-not (Test-Path $src)) { Write-Error "Source missing: $src"; exit 1 }
    New-Item -ItemType Directory -Force -Path (Split-Path $dst -Parent) | Out-Null
    Copy-Item -Path $src -Destination $dst -Recurse -Force
    Write-Output "[COPY] $srcRel -> $dstRel"
}

function New-FromTemplate($templateFile, $targetRel, $desc) {
    $tpl = Join-Path $TemplateDir $templateFile; $tgt = Join-Path $ProjectRoot $targetRel
    if (-not (Test-Path $tpl)) { Write-Error "Template missing: $tpl"; exit 1 }
    if ((Test-Path $tgt) -and -not $Force) { Write-Output "[SKIP] $targetRel (use -Force)"; return }
    if ($DryRun) { Write-Output "[DRY-RUN] Generate: $templateFile -> $targetRel ($desc)"; return }
    $c = Get-Content $tpl -Raw; foreach ($k in $Placeholders.Keys) { $c = $c.Replace($k, $Placeholders[$k]) }
    foreach ($k in $ManifestPlaceholders.Keys) { $c = $c.Replace($k, $ManifestPlaceholders[$k]) }
    New-Item -ItemType Directory -Force -Path (Split-Path $tgt -Parent) | Out-Null
    Set-Content $tgt $c -NoNewline
    Write-Output "[GEN] $targetRel"
}

Write-Output "`n=== Step 1: Universal Assets ==="
Copy-Universal "rules" "rules" "8 rules, 44 entries"
Copy-Universal "schemas" "schemas" "18 JSON Schema files"
Copy-Universal "docs/agent-runtime/operating-model.md" "docs/agent-runtime/operating-model.md" "Operating model"
Copy-Universal "docs/agent-runtime/integration-contracts.md" "docs/agent-runtime/integration-contracts.md" "Integration contracts"
Copy-Universal "docs/agent-runtime/verification-gates.md" "docs/agent-runtime/verification-gates.md" "Verification gates"
Copy-Universal "docs/agent-runtime/runtime-invariants.md" "docs/agent-runtime/runtime-invariants.md" "Runtime invariants"
Copy-Universal "docs/agent-runtime/reviewer-playbook.md" "docs/agent-runtime/reviewer-playbook.md" "Reviewer playbook"
Copy-Universal "docs/agent-runtime/sub-agent-dispatch-protocol.md" "docs/agent-runtime/sub-agent-dispatch-protocol.md" "SADP protocol"
Copy-Universal "docs/agent-runtime/dispatch-model-profiles.md" "docs/agent-runtime/dispatch-model-profiles.md" "Model profiles"
Copy-Universal "docs/agent-runtime/lessons-learned.md" "docs/agent-runtime/lessons-learned.md" "Lessons learned"Copy-Universal "docs/agent-runtime/sub-agent-dispatch-protocol.md" "docs/agent-runtime/sub-agent-dispatch-protocol.md" "Sub-agent dispatch protocol"
Copy-Universal "docs/agent-runtime/negative-acceptance-tests.md" "docs/agent-runtime/negative-acceptance-tests.md" "Negative tests"
Copy-Universal "docs/agent-runtime/negative-test-fixtures" "docs/agent-runtime/negative-test-fixtures" "30 fixtures"
# Self-copy templates for re-bootstrap (skip in dry-run)
if (-not $DryRun) {
    $tplDest = Join-Path $ProjectRoot "templates\runtime-bootstrap"
    New-Item -ItemType Directory -Force -Path $tplDest | Out-Null
    Copy-Item -Path "$ScriptDir\*" -Destination $tplDest -Recurse -Force
    Write-Output "[COPY] Bootstrap templates self-copied"
} else {
    Write-Output "[DRY-RUN] Copy: templates/runtime-bootstrap/ -> templates/runtime-bootstrap/"
}

Write-Output "`n=== Step 2: Project-Specific Files ==="
New-FromTemplate "AGENTS.template.md" "AGENTS.md" "Agent entry point"
New-FromTemplate "capability-inventory.template.md" "docs/agent-runtime/capability-inventory.md" "Capability inventory"
New-FromTemplate "tool-policy.template.md" "docs/agent-runtime/tool-policy.md" "Tool policy"

# --- Governance Manifest (hash-locked, generated after all files exist) ---
$p0Hash = (Get-FileHash (Join-Path $ProjectRoot "rules\core.md") -Algorithm SHA256).Hash
$sadpHash = (Get-FileHash (Join-Path $ProjectRoot "docs\agent-runtime\sub-agent-dispatch-protocol.md") -Algorithm SHA256).Hash
$agentsHash = (Get-FileHash (Join-Path $ProjectRoot "AGENTS.md") -Algorithm SHA256).Hash
$ManifestPlaceholders = @{
    "{{P0_HASH}}" = $p0Hash
    "{{GATE0_HASH}}" = $sadpHash
    "{{VETO_HASH}}" = $sadpHash
    "{{PROTECTED_HASH}}" = $agentsHash
    "{{CUMULATIVE_HASH}}" = $sadpHash
}
New-FromTemplate "governance-manifest.template.md" "docs/agent-runtime/governance-manifest.md" "Governance manifest (hash-locked)"

Write-Output "`n=== Step 3: Verification ==="
if ($DryRun) { Write-Output "[DRY-RUN] Done."; exit 0 }

$unresolved = Select-String -Path (Join-Path $ProjectRoot "AGENTS.md") -Pattern "\{\{" -SimpleMatch 2>$null
if ($unresolved) { Write-Error "FAIL: Unresolved placeholders in AGENTS.md" } else { Write-Output "[OK] AGENTS.md: clean" }

$inv = Join-Path $ProjectRoot "docs\agent-runtime\capability-inventory.md"
$n = (Select-String -Path $inv -Pattern "^## \d+\." 2>$null).Count
if ($n -ge 10) { Write-Output "[OK] Capabilities: $n" } else { Write-Error "FAIL: Only $n capabilities" }

Write-Output "`n=== Bootstrap Complete ==="
Write-Output "Next: 1) Register project capabilities (#11+) 2) Configure platform assets 3) Reviewer sign-off"
Write-Output "See INSTANTIATION.md for details."