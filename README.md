[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/steimerbyte)

> ⭐ If you find this useful, consider [supporting me on Ko-fi](https://ko-fi.com/steimerbyte)!

<img src="https://storage.ko-fi.com/cdn/generated/fhfuc7slzawvi/2026-04-23_rest-162bec27f642a562eb8401eb0ceb3940-onjpojl8.jpg" width="250" alt="steimerbyte" style="border-radius: 5%; margin: 16px 0; max-width: 100%;"/>

# RK Gaming Keyboard Configuration App (Linux Standalone) v1.1

> **Release 1.1**: Terminal-based launcher with automatic browser opening!

This is a **standalone, offline-capable Linux application** for configuring RK Gaming keyboards. It mirrors the official web-based driver (drive2.rkgaming.com) and wraps it in a lightweight local environment, solving the issue of WebHID not working in standard file-based browsing.

## 🚀 Features

- **Full Linux Support**: Runs flawlessly on most Linux distributions.
- **Offline Capable**: All website assets are bundled locally; no internet connection required after download.
- **WebHID Support**: Communicates directly with your keyboard via USB.
- **Terminal Launcher (v1.1)**: Opens a new terminal window displaying the server URL with one click.
- **Auto-Browser Launch**: Automatically opens Brave/Chromium via `xdg-open`.
- **Dynamic Port Allocation**: No port conflicts - always uses a free port.
- **Native Experience**: Runs in a dedicated browser window ("App Mode") without address bars or tabs.

## 📋 Prerequisites

- **Python 3** (Pre-installed on almost all Linux distros).
- **A Chromium-based Browser**: WebHID support is required. Supported browsers include:
    - Google Chrome (Native & Flatpak)
    - Chromium (Native & Flatpak)
    - **Brave** (Native, Flatpak & Snap)
    - Microsoft Edge (Native & Flatpak)
    - Opera / Vivaldi

## 📥 Installation & Usage

### Option 1: AppImage (Recommended) - v1.1

The **Terminal AppImage** opens a new terminal with the server URL and auto-launches your browser.

1. **Download** `RK_Gaming_Keyboard_Terminal.AppImage` from this repository.
2. **Make it executable**:
    ```bash
    chmod +x RK_Gaming_Keyboard_Terminal.AppImage
    ```
3. **Run it**:
    ```bash
    ./RK_Gaming_Keyboard_Terminal.AppImage
    ```

**What happens:**
```
╔════════════════════════════════════════════════════════╗
║         RK Gaming Keyboard Configuration             ║
╚════════════════════════════════════════════════════════╝

🌐 Server running at: http://localhost:51901

📋 Open in Brave/Chromium - click link above!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  Keep this terminal open while using the app
   Press Ctrl+C to stop the server
```

### Option 2: Original AppImage (with browser selection)

The original AppImage lets you choose which browser to use:

1. Download `RK_Gaming_Keyboard.AppImage`.
2. Make executable and run:
    ```bash
    chmod +x RK_Gaming_Keyboard.AppImage
    ./RK_Gaming_Keyboard.AppImage
    ```

### Option 3: Desktop Integration (Install to Menu)

If you want the app to appear in your system's Start Menu / Application Launcher:

1. Clone or download this repository.
2. Open a terminal in the folder.
3. Run the setup script:
    ```bash
    ./setup_linux.sh
    ```
4. Search for **"RK Gaming Keyboard"** in your application menu.

### Option 4: Manual / Portable (Source)

You can run the Python script directly from the source code:

1. Ensure you have Python 3 installed.
2. Run the app:
    ```bash
    ./rk_app.py
    ```

## 🛠 Troubleshooting

- **"No device found"**:
    - Ensure your keyboard is connected via **USB** (wired mode).
    - WebHID requires permission to access USB devices. Usually, modern Linux distros handle this automatically. If not, you may need to check your `udev` rules.
    - Try running the browser/app as root (not recommended, but good for testing if it's a permission issue).

- **"No supported browser found"**:
    - The app looks for standard executables (`google-chrome`, `chromium-browser`, `brave`, `brave-browser`, etc.) and Flatpaks. Ensure you have one installed.

- **Port already in use**:
    - The Terminal AppImage (v1.1) uses dynamic port allocation - this shouldn't happen anymore. If it does, kill the process using that port or use the original AppImage.

## 📝 Changelog

### v1.1 (2026-05-04)
- Added **Terminal AppImage** with automatic browser launching
- Dynamic port allocation to avoid conflicts
- Opens new terminal window with clickable server URL
- Auto-detects terminal emulator (gnome-terminal, konsole, xfce4-terminal, etc.)

### v1.0 (2026-04-23)
- Initial release
- Basic AppImage with browser selection dialog
- Offline-capable web UI

## ⚖️ Disclaimer

This project is an unofficial wrapper and mirror of the RK Gaming configuration software. It is not affiliated with, endorsed by, or connected to RK Gaming. All original web assets belong to their respective owners.
