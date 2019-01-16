from flask import Flask
from flask import render_template
from flask import request
from .carControl import *
from .Camera_Server import *
#flask run --host=0.0.0.0 --port=8080
PORT_NUMBER = 8080

app = Flask(__name__)

@app.route('/')
def main():

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

    if (command == 'left'):
        blink()

    return ''

if __name__ == '__main__':
    app.run(debug=True)
