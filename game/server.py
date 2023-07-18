import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        super().end_headers()

with socketserver.TCPServer(("", 8000), CustomHandler) as httpd:
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
