# Name:    GlobalNameCloudAPI
# Purpose: Execute the GlobalNameCloudAPI program

######################### Parameters ##########################
param(
    $fullname = '',  
    $license = '', 
    [switch]$quiet = $false
    )

########################## Main ############################
Write-Host "`n================== Melissa Global Name Cloud API ====================`n"

# Get license (either from parameters or user input)
if ([string]::IsNullOrEmpty($license) ) {
  $license = Read-Host "Please enter your license string"
}

# Check for License from Environment Variables 
if ([string]::IsNullOrEmpty($license) ) {
  $license = $env:MD_LICENSE
}

if ([string]::IsNullOrEmpty($license)) {
  Write-Host "`nLicense String is invalid!"
  Exit
}

# Run project
if ([string]::IsNullOrEmpty($fullname)) {
  python3 GlobalNamePython3.py --license $license 
}
else {
  python3 GlobalNamePython3.py --license $license --fullname $fullname
}
