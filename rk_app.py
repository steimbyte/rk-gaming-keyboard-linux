#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys
import subprocess
import threading
import socket
import shutil
import tempfile
import time
import signal

# Configuration
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SITE_DIR = os.path.join(BASE_DIR, "site/drive2.rkgaming.com")
APP_TITLE = "RK Gaming Keyboard"

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def do_GET(self):
        # Redirect all non-file requests to index.html for SPA routing
        path = self.path.split('?')[0]
        full_path = os.path.join(SITE_DIR, path.lstrip('/'))
        if not os.path.exists(full_path):
            self.path = '/index.html'
        return super().do_GET()

    def log_message(self, format, *args):
        # Suppress logging to keep console clean
        pass

def start_server(port, stop_event):
    with socketserver.TCPServer(("127.0.0.1", port), SPAHandler) as httpd:
        httpd.timeout = 1
        while not stop_event.is_set():
            httpd.handle_request()

def detect_browsers():
    """Returns a list of available (name, executable_path_or_command) tuples."""
    # Standard binary check
    known_browsers = [
        ("Google Chrome", "google-chrome"),
        ("Google Chrome (Stable)", "google-chrome-stable"),
        ("Chromium", "chromium-browser"),
        ("Chromium (Alt)", "chromium"),
        ("Brave", "brave-browser"),
        ("Microsoft Edge", "microsoft-edge"),
        ("Vivaldi", "vivaldi"),
        ("Opera", "opera")
    ]
    
    # Flatpak App IDs
    flatpak_browsers = [
        ("Brave (Flatpak)", "com.brave.Browser"),
        ("Google Chrome (Flatpak)", "com.google.Chrome"),
        ("Chromium (Flatpak)", "org.chromium.Chromium"),
        ("Microsoft Edge (Flatpak)", "com.microsoft.Edge"),
        ("Ungoogled Chromium (Flatpak)", "com.github.Eloston.UngoogledChromium")
    ]

    available = []
    
    # Check standard binaries
    for name, binary in known_browsers:
        path = shutil.which(binary)
        if path:
            if path not in [p for _, p in available]:
                available.append((name, path))

    # Check Flatpaks
    if shutil.which("flatpak"):
        try:
            # List installed flatpaks
            output = subprocess.check_output(["flatpak", "list", "--app", "--columns=application"], text=True)
            installed_ids = output.splitlines()
            
            for name, app_id in flatpak_browsers:
                if app_id in installed_ids:
                    # For flatpaks, the "path" is actually a command list, but we'll handle that in get_browser_command
                    # We store it as a special string prefix or just the command string.
                    # Simplest is to store the full run command as a string, but Popen needs list if shell=False.
                    # Let's verify how we construct the final command.
                    # Currently get_browser_command returns a list: [exe, flags...]
                    # If we return "flatpak run com.brave.Browser", that's one string.
                    # We'll use a special marker or just detecting spaces.
                    available.append((name, f"flatpak run {app_id}"))
        except Exception:
            pass

    return available

def show_browser_selection_dialog(browsers):
    """
    Attempts to show a GUI dialog to select a browser.
    Falls back to simple heuristics if no GUI tools are available.
    """
    
    # Try Zenity (GNOME/GTK)
    if shutil.which("zenity"):
        cmd = [
            "zenity", "--list",
            "--title=" + APP_TITLE,
            "--text=Select a browser to launch the app:",
            "--column=Browser", "--column=Path",
            "--hide-column=2",
            "--height=300"
        ]
        for name, path in browsers:
            cmd.extend([name, path])
        
        try:
            result = subprocess.check_output(cmd, text=True).strip()
            if result:
                # Result is just the name (column 1) because column 2 is hidden? 
                # Actually zenity returns the selected row's text from the first column by default unless --print-column is used.
                # But we need the path. Let's map name back to path.
                for name, path in browsers:
                    if name == result:
                        return path
                return None
        except subprocess.CalledProcessError:
            return None # User cancelled

    # Try KDialog (KDE)
    if shutil.which("kdialog"):
        cmd = [
            "kdialog", "--title", APP_TITLE,
            "--menu", "Select a browser to launch the app:",
        ]
        for i, (name, path) in enumerate(browsers):
            cmd.extend([path, name]) # kdialog uses 'tag item' format
            
        try:
            result = subprocess.check_output(cmd, text=True).strip()
            if result:
                return result
        except subprocess.CalledProcessError:
            return None

    # Try Tkinter (Python Native)
    try:
        import tkinter as tk
        from tkinter import simpledialog
        
        root = tk.Tk()
        root.withdraw() # Hide main window
        
        # Simple listbox dialog
        dialog = tk.Toplevel(root)
        dialog.title("Select Browser")
        dialog.geometry("300x250")
        
        tk.Label(dialog, text="Select a browser to launch the app:").pack(pady=10)
        
        listbox = tk.Listbox(dialog)
        listbox.pack(expand=True, fill="both", padx=10)
        
        for name, path in browsers:
            listbox.insert(tk.END, name)
            
        selected_path = [None]
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                index = selection[0]
                selected_path[0] = browsers[index][1]
                dialog.destroy()
                
        tk.Button(dialog, text="OK", command=on_select).pack(pady=10)
        
        dialog.transient(root)
        dialog.grab_set()
        root.wait_window(dialog)
        return selected_path[0]
        
    except ImportError:
        pass
    except Exception:
        pass

    # Fallback: Just return the first one found
    return browsers[0][1]

def get_browser_command(url, user_data_dir):
    available_browsers = detect_browsers()
    
    if not available_browsers:
        return None
        
    # If only one browser, just use it
    if len(available_browsers) == 1:
        selected_browser_path = available_browsers[0][1]
    else:
        # If multiple, try to ask user
        selected = show_browser_selection_dialog(available_browsers)
        if selected:
            selected_browser_path = selected
        else:
            # Cancelled or failed, default to first
            selected_browser_path = available_browsers[0][1]

    # Flags for app-like experience
    # Check if selected_browser_path is a flatpak command string
    base_cmd = []
    if selected_browser_path.startswith("flatpak run"):
        base_cmd = selected_browser_path.split() # ['flatpak', 'run', 'app.id']
    else:
        base_cmd = [selected_browser_path]

    return base_cmd + [
        f"--app={url}",
        f"--user-data-dir={user_data_dir}",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,800"
    ]

def main():
    if not os.path.exists(SITE_DIR):
        print(f"Error: Site directory not found at {SITE_DIR}")
        sys.exit(1)

    port = find_free_port()
    url = f"http://localhost:{port}"
    
    print(f"Starting {APP_TITLE}...")
    
    # Start Server
    stop_event = threading.Event()
    server_thread = threading.Thread(target=start_server, args=(port, stop_event))
    server_thread.daemon = True
    server_thread.start()
    
    # Wait a moment for server to start
    time.sleep(0.5)
    
    # Prepare browser
    temp_profile = tempfile.mkdtemp(prefix="rk_keyboard_app_")
    cmd = get_browser_command(url, temp_profile)
    
    if not cmd:
        print("Error: No supported browser found (Chrome/Chromium/Edge).")
        print(f"Server is running at {url}. Open this manually if you wish.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        return

    print(f"Launching browser: {cmd[0]}")
    
    try:
        # Run browser and wait for it to close
        process = subprocess.Popen(cmd)
        process.wait()
    except KeyboardInterrupt:
        print("\nStopping...")
        if process:
            process.terminate()
    finally:
        print("Cleaning up...")
        stop_event.set()
        server_thread.join(timeout=2)
        try:
            shutil.rmtree(temp_profile, ignore_errors=True)
        except:
            pass
        print("Done.")

if __name__ == "__main__":
    main()
