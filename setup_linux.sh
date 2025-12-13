#!/bin/bash

# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Path to the icon (using the downloaded logo)
ICON_PATH="$DIR/site/drive2.rkgaming.com/assets/logo-DgpZE-f6.png"
EXEC_PATH="$DIR/rk_app.py"

# Create the .desktop file content
DESKTOP_ENTRY="[Desktop Entry]
Version=1.0
Type=Application
Name=RK Gaming Keyboard
Comment=Configuration tool for RK Gaming Keyboards
Exec=python3 \"$EXEC_PATH\"
Icon=$ICON_PATH
Terminal=false
Categories=Utility;HardwareSettings;
StartupNotify=true"

# Define the desktop file location
DESKTOP_FILE="$HOME/.local/share/applications/rk-gaming-keyboard.desktop"

# Write the file
echo "$DESKTOP_ENTRY" > "$DESKTOP_FILE"

# Make the app script executable
chmod +x "$EXEC_PATH"

# Update desktop database
update-desktop-database "$HOME/.local/share/applications" 2>/dev/null

echo "Installation complete!"
echo "You can now find 'RK Gaming Keyboard' in your application menu."

