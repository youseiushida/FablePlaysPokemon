param(
    [Parameter(Mandatory = $true)]
    [string]$Url
)

$ErrorActionPreference = "Stop"

try {
    $json = [Console]::In.ReadToEnd()

    if ([string]::IsNullOrWhiteSpace($json)) {
        exit 0
    }

    Invoke-RestMethod `
        -Uri $Url `
        -Method Post `
        -ContentType "application/json" `
        -Body $json `
        -TimeoutSec 1 `
        | Out-Null
}
catch {
    # stdout/stderr に何も出さない
}

exit 0