[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/steimerbyte)

> ⭐ If you find this useful, consider [supporting me on Ko-fi](https://ko-fi.com/steimerbyte)!

<img src="https://storage.ko-fi.com/cdn/generated/fhfuc7slzawvi/2026-04-23_rest-162bec27f642a562eb8401eb0ceb3940-onjpojl8.jpg" alt="steimerbyte" style="border-radius: 8px; margin: 16px 0; max-width: 100%;"/>

# RK Gaming Keyboard Configuration App (Linux Standalone)

This is a **standalone, offline-capable Linux application** for configuring RK Gaming keyboards. It mirrors the official web-based driver (drive2.rkgaming.com) and wraps it in a lightweight local environment, solving the issue of WebHID not working in standard file-based browsing.

## 🚀 Features

- **Full Linux Support**: Runs flawlessly on most Linux distributions.
- **Offline Capable**: All website assets are bundled locally; no internet connection required after download.
- **WebHID Support**: Communicates directly with your keyboard via USB.
- **Browser Selection**: Automatically detects installed Chromium-based browsers (including Flatpaks) and lets you choose which one to use.
- **Native Experience**: Runs in a dedicated window ("App Mode") without address bars or tabs.

## 📋 Prerequisites

- **Python 3** (Pre-installed on almost all Linux distros).
- **A Chromium-based Browser**: WebHID support is required. Supported browsers include:
    - Google Chrome (Native & Flatpak)
    - Chromium (Native & Flatpak)
    - Brave (Native & Flatpak)
    - Microsoft Edge (Native & Flatpak)
    - Opera / Vivaldi

## 📥 Installation & Usage

### Option 1: AppImage (Recommended)

The easiest way to run the app. It's a single file containing everything you need.

1.  **Download** `RK_Gaming_Keyboard.AppImage` from this repository.
2.  **Make it executable**:
    ```bash
    chmod +x RK_Gaming_Keyboard.AppImage
    ```
3.  **Run it**:
    ```bash
    ./RK_Gaming_Keyboard.AppImage
    ```

### Option 2: Desktop Integration (Install to Menu)

If you want the app to appear in your system's Start Menu / Application Launcher:

1.  Clone or download this repository.
2.  Open a terminal in the folder.
3.  Run the setup script:
    ```bash
    ./setup_linux.sh
    ```
4.  Search for **"RK Gaming Keyboard"** in your application menu.

### Option 3: Manual / Portable (Source)

You can run the Python script directly from the source code:

1.  Ensure you have Python 3 installed.
2.  Run the app:
    ```bash
    ./rk_app.py
    ```

## 🛠 Troubleshooting

- **"No device found"**:
    - Ensure your keyboard is connected via **USB** (wired mode).
    - WebHID requires permission to access USB devices. Usually, modern Linux distros handle this automatically. If not, you may need to check your `udev` rules.
    - Try running the browser/app as root (not recommended, but good for testing if it's a permission issue).

- **"No supported browser found"**:
    - The app looks for standard executables (`google-chrome`, `chromium-browser`, `brave-browser`, etc.) and Flatpaks. Ensure you have one installed.

## ⚖️ Disclaimer

This project is an unofficial wrapper and mirror of the RK Gaming configuration software. It is not affiliated with, endorsed by, or connected to RK Gaming. All original web assets belong to their respective owners.
