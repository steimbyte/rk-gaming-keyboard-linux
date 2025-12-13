import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8000
DIRECTORY = "site/drive2.rkgaming.com"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Redirect all non-file requests to index.html for SPA routing
        path = self.path.split('?')[0]
        full_path = os.path.join(DIRECTORY, path.lstrip('/'))
        if not os.path.exists(full_path):
            self.path = '/index.html'
        return super().do_GET()

print(f"Serving at http://localhost:{PORT}")
print("Opening browser...")

# Change directory to workspace root if needed, but the script handles directory param
# We assume the script is run from the workspace root

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
except OSError as e:
    print(f"Error: {e}")
    print("Try a different port or check if the port is in use.")

