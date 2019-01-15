from flask import Flask
from flask import render_template
from flask import request
from .carControl import *
from .Camera_Server import *
#flask run --host=0.0.0.0 --port=8080
PORT_NUMBER = 8080

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template('./index.html')

@app.route('/command')
def command():
    command = request.args.get('command')
    if (command == 'stop'):
        stop()
        
    if (command == 'rightforward'):
        rightforward()
            
    if (command == 'leftforward'):
        leftforward()
            
    
    if (command == 'forward'):
        forward()
    
    if (command == 'backward'):
        backward()

    command = request.args.get('command')
    if (command == 'left'):
        blink()

    return ''

if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/python

""" 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import parse_qs
from carControl import *
from Camera_Server import *

PORT_NUMBER = 8080
carController = carControl()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        with open('index.html', 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)
        
        #carController.blink()
        #carController.drive()
        
        self.wfile.write(parse_qs(self.path))

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
        cmr_Thread = Camera_Server()
        cmr_Thread = Camera_Server()
        cmr_Thread.start()
	
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
    
"""