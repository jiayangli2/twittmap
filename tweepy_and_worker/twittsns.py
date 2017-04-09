#import BaseHTTPServer.BaseHTTPRequestHandler
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import http.server
import cgitb
import requests
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.query_string = self.rfile.read(int(self.headers['Content-Length']))
        self.args = dict(cgi.parse_qsl(self.query_string))
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Content-type: text/html<BR><BR>");
        self.wfile.write("<HTML>POST OK.<BR><BR>");

def main():
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
