#!/bin/bash
# RK Gaming Keyboard - Server Starter mit xdg-open (Brave)
cd "$(dirname "$0")"

PORT=8000
echo "=========================================="
echo "  RK Gaming Keyboard - Server Starter"
echo "=========================================="
echo "Starting server at http://localhost:$PORT"
echo "Opening Brave via xdg-open..."
echo ""

# Server starten + Browser in einem Rutsch
python3 -c "
import http.server, socketserver, os, subprocess, time

PORT = 8000
DIR = 'site/drive2.rkgaming.com'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def do_GET(self):
        path = self.path.split('?')[0]
        full = os.path.join(DIR, path.lstrip('/'))
        if not os.path.exists(full):
            self.path = '/index.html'
        return super().do_GET()

print(f'Server running on http://localhost:{PORT}')
subprocess.run(['xdg-open', f'http://localhost:{PORT}'])

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Press Ctrl+C to stop')
    httpd.serve_forever()
" 2>&1
