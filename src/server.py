"""
UrjaCycle AI - Standalone HTTP REST & Dashboard Server
Author: Bhomesh Razdan (Lead Architect)
"""

import http.server
import socketserver
import json
import urllib.parse
import os
import sys

from .lambda_handlers import (
    handler_classify_waste,
    handler_calculate_solar,
    handler_get_ev_slots,
    handler_cedar_auth
)

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

class UrjaCycleHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)
        params = {k: v[0] for k, v in query.items()}
        event = {"httpMethod": "GET", "path": path, "queryStringParameters": params}

        if path == "/api/waste/classify":
            res = handler_classify_waste(event)
        elif path == "/api/solar/calculate":
            res = handler_calculate_solar(event)
        elif path == "/api/ev/slots":
            res = handler_get_ev_slots(event)
        elif path.startswith("/api/"):
            res = {"statusCode": 404, "body": json.dumps({"error": f"Endpoint {path} not found"})}
        else:
            return super().do_GET()

        self._send_api(res)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        event = {"httpMethod": "POST", "path": path, "body": body}

        if path == "/api/auth/cedar":
            res = handler_cedar_auth(event)
        else:
            res = {"statusCode": 404, "body": json.dumps({"error": f"Endpoint {path} not found"})}

        self._send_api(res)

    def _send_api(self, res):
        self.send_response(res.get("statusCode", 200))
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        b = res.get("body", "{}")
        self.wfile.write((b if isinstance(b, str) else json.dumps(b)).encode("utf-8"))

def run_server(port: int = 8082):
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), UrjaCycleHandler) as httpd:
        print(f"[UrjaCycle AI] Running at http://localhost:{port} (Architect: Bhomesh Razdan)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Stopping...")

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8082
    run_server(p)
