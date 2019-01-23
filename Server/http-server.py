
from flask import Flask
from flask import render_template
from flask import request
from .carControl import *
from .Camera_Server import *

"""
cd ~/raspberry-car; export FLASK_APP=http-server.py; flask run --host=0.0.0.0 --port=8080;

"""
PORT_NUMBER = 8080
TEMPLATES_AUTO_RELOAD = True

app = Flask(__name__)

@app.route('/')
def main():

    return render_template('./index.html')

@app.route('/command')
def command():
    command = request.args.get('command')

    data = {
        'direction': request.args.get('direction'),
        'speed': request.args.get('speed'),
        'turning_angle': request.args.get('turning_angle')
        }
    
    
    if (command == 'camera'):
        camera_data = {
        'camera_up_down': request.args.get('camera_up_down'),
        'camera_left_right': request.args.get('camera_left_right'),

        }    
        resp = camera(**camera_data)
        return resp

    if (command == 'run'):
        resp = runner(**data)
        return resp

    if (command == 'stop'):
        stop()
        return ''

    if (command == 'buzz'):
        buzz()
        return ''

    if (command == 'blink'):
        blink()
        return ''

    if (command == 'rightforward'):
        rightforward()
        return ''

    if (command == 'leftforward'):
        leftforward()
        return ''

    if (command == 'forward'):
        resp = forward()
        return resp

    if (command == 'backward'):
        resp = backward()
        return ''

    return ''

if __name__ == '__main__':
    app.run(debug=False )
