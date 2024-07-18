from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Hello! Current time is: {current_time}"
        
        self.wfile.write(message.encode())
        return