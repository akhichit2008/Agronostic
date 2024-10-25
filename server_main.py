import http.server
from http.server import SimpleHTTPRequestHandler
import socketserver

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow any origin
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        super().end_headers()

PORT = 8000  # Choose your desired port
with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
