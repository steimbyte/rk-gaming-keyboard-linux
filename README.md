# RK Gaming Keyboard Configuration App (Linux Standalone)

This is a local, standalone version of the RK Gaming keyboard configuration site. It wraps the website in a lightweight local server and launches it in a dedicated browser window (Chrome/Chromium app mode), providing a native application feel with full WebHID support for device communication.

## Prerequisites

- **Python 3** (The AppImage uses the system Python 3).
- **Chromium-based Browser**: Google Chrome, Chromium, Brave, or Edge. (Required for WebHID support).

## Installation / Usage

### Option 1: AppImage (Recommended)

A single-file executable is available.

1.  Download or locate `RK_Gaming_Keyboard.AppImage` in this folder.
2.  Make it executable (if not already):
    ```bash
    chmod +x RK_Gaming_Keyboard.AppImage
    ```
3.  Run it:
    ```bash
    ./RK_Gaming_Keyboard.AppImage
    ```

### Option 2: Install Script

To integrate it into your desktop environment (start menu):

1.  Open a terminal in this folder.
2.  Run the setup script:
    ```bash
    ./setup_linux.sh
    ```
3.  The app **"RK Gaming Keyboard"** should now appear in your application menu.

### Option 3: Manual / Portable

You can run the python script directly:

```bash
./rk_app.py
```

## How It Works

- `rk_app.py`: This is the main runtime. It starts a local web server on a random free port and launches your installed browser in "App Mode" (`--app`), creating a standalone window without address bars or tabs. It uses a temporary user profile to ensure a clean environment.
- `site/`: Contains the mirrored website assets.

## Troubleshooting

- **Device not found?** Ensure your browser has permission to access USB/HID devices. On Linux, you might need to update your `udev` rules for the keyboard if the browser cannot see it (though usually, the browser handles this if run as a regular user).
- **No browser opens?** Install `google-chrome` or `chromium`.
