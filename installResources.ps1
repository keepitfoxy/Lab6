# PowerShell script to install necessary Python packages

# Install pip if not installed
python -m ensurepip --upgrade

# Install necessary Python packages
pip install pyinstaller
pip install PyQt5
pip install jsonschema
pip install xmltodict
pip install pyyaml

Write-Output "All required packages have been installed."
