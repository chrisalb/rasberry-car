var carController = function () {

    this.data = {
        command: '',
        speed: '',
    };

    this.init();
}

carController.prototype = {
    init: function () {
        this.listenEvents();
    },

    listenEvents: function () {
        var self = this;

        var leftBtn = document.getElementById('left');

        leftBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'left';
            self.send();
        });

        leftBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var rightBtn = document.getElementById('right');
        rightBtn.addEventListener('click', function (ev) {
            self.data.command = 'right';
        });

        var forwardBtn = document.getElementById('forward');
        forwardBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'forward';
            self.send();
        });
        forwardBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var backwardBtn = document.getElementById('backward');
        backwardBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'backward';
            self.send();
        });

        backwardBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var leftforwardBtn = document.getElementById('leftforward');
        leftforwardBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'leftforward';
            self.send();
        });

        leftforwardBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var rightforwardBtn = document.getElementById('rightforward');
        rightforwardBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'rightforward';
            self.send();
        });

        rightforwardBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var stopBtn = document.getElementById('stop');
        stopBtn.addEventListener('click', function (ev) {
            self.data.command = 'stop';
            self.send();
        });
    },

    setMoveSpeed: function (speed) {

        this.data.speed = (speed / 3);
        this.send();

        this.data.speed = (speed / 3 * 2);
        this.send();

        this.data.speed = (speed);
        this.send();
    },
    get: function () {
        var request = new XMLHttpRequest();

        request.open('GET', '/?command=' + this.data.command);
        request.send();
    },

    send: function () {
        var request = new XMLHttpRequest;

        request.open('GET', '/command?command=' + this.data.command);
        request.send();
    }
}

document.addEventListener('DOMContentLoaded', function () {
    carcontroller = new carController();
});