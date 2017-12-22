#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import subprocess as sp

main_html_page =  """
<html>
<body>
<h1>Web Controller</h1>

<form action="/" method="post">
  <p>Direction</p>
  <input type="radio" name="direction" value="forward" checked> Forward<br><br>
  <input type="radio" name="direction" value="backward"> Backward<br><br>
  <input type="submit" value="Submit">
</form>

</body>
</html>
"""

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(main_html_page)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        command = post_data.split('=')[0]
        direction = post_data.split('=')[1]
        print("post_data: %s command: %s direction: %s" % (post_data, command, direction))
        command = ('/usr/bin/python /home/pi/Documents/Roomba_Snow_Plow/move_motor.py --direction %s' % direction)
        output = sp.check_output(command, shell=True)
        self._set_headers()
        self.wfile.write(main_html_page)        
                
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run(port = 8001)