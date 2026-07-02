import http.server
import socketserver

PORT = 80

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Mujahid, aap yahan apna custom message dekh sakte hain
        self.wfile.write(b"<h1>Hello this is Mujahid! Congratulations Python App is running inside Docker! \ud83d\ude80</h1>")
        self.wfile.write(b"<h1>This is my first ci cd pipeline setup  \ud83d\ude80</h1>")

print(f"Server starting on port {PORT}...")
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()
