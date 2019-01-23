var carController = function () {

    this.data = {
        command: '',
        speed: 100,
        direction: 0,
        turning_angle: 1500,
        camera_left_right: 1500,
        camera_up_down: 1500,
    };

    this.init();
}

carController.prototype = {
    init: function () {
        this.listenEvents();
    },

    initSlider: function () {
        var self = this;
        $(".circle-slider").roundSlider({
            sliderType: "min-range",
            radius: 430,
            showTooltip: false,
            width: 16,
            value: 75,
            handleSize: 0,
            circleShape: "half-top",
            startAngle: 50,
            endAngle: "+50",
            value: 50,

            create: function (v) {

            },
            drag: function (v) {
                self.data.command = 'run';
                self.data.direction = 0;
                self.data.speed = 400;
                self.data.turning_angle = v.value * 30;
                self.send();
            },
            stop: function (v) {
                self.data.command = 'stop';
                self.send();
                this.value = 50;
                this.startAngle = 50
            }
        });

    },
    listenEvents: function () {
        var self = this;

        var forwardBtn = document.getElementById('forward');
        forwardBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'forward';
            self.send();
        });
        forwardBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        forwardBtn.addEventListener('touchstart', function (ev) {
            self.data.command = 'forward';
            self.send();
        });

        forwardBtn.addEventListener('touchend', function (ev) {
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

        var buzzBtn = document.getElementById('buzz');
        buzzBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'buzz';
            self.send();
        });

        buzzBtn.addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

        var blinkBtn = document.getElementById('blink');
        blinkBtn.addEventListener('mousedown', function (ev) {
            self.data.command = 'blink';
            self.send();
        });

        blinkBtn.addEventListener('mouseup', function (ev) {
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
    ultrasonic: function (distance) {
        /*         var ultradisplay = document.getElementById('ultradisplay');
                var prev = ultradisplay.innerText;
                ultradisplay.innerText = prev + " *** " + distance; */
    },

    send: function () {
        var self = this;
        var request = new XMLHttpRequest;
        request.onreadystatechange = function () {
            if (request.readyState === 4) {
                self.ultrasonic(request.response);
            }
        }
        request.open('GET',
            '/command?command=' + this.data.command +
            '&direction=' + this.data.direction +
            '&speed=' + this.data.speed +
            '&camera_left_right=' + this.data.camera_left_right +
            '&camera_up_down=' + this.data.camera_up_down +
            '&turning_angle=' + this.data.turning_angle +
            '&blink=' + this.data.blink

        );
        request.send();
    }
}

document.addEventListener('DOMContentLoaded', function () {

    carcontroller = new carController();
});