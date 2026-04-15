#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import sys
import os
import json
import base64
from datetime import datetime
from pathlib import Path

PORT = 8000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

pictures_dir = Path(SCRIPT_DIR) / "pictures"
pictures_dir.mkdir(exist_ok=True)


class CaptureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/save-capture":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            try:
                data = json.loads(body.decode("utf-8"))
                image_data = data.get("image", "")

                if ";base64," in image_data:
                    image_data = image_data.split(",")[1]

                image_bytes = base64.b64decode(image_data)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"goldface_{timestamp}.jpg"
                filepath = pictures_dir / filename

                with open(filepath, "wb") as f:
                    f.write(image_bytes)

                response = json.dumps({"success": True, "filename": filename})
                response_bytes = response.encode("utf-8")

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response_bytes)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(response_bytes)
                print(f"Saved: {filename}")

            except Exception as e:
                print(f"Error: {e}")
                response = json.dumps({"success": False, "error": str(e)})
                response_bytes = response.encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response_bytes)))
                self.end_headers()
                self.wfile.write(response_bytes)
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


class QuietTCPServer(socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


with QuietTCPServer(("", PORT), CaptureHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Captured photos saved to: {pictures_dir}")
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    print("\nPress Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
