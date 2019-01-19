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
        this.initSlider();
        this.listenEvents();
    },

    initSlider: function () {
        var self = this;
        $(".circle-slider").roundSlider({
            sliderType: "min-range",
            radius: 130,
            steps: 50,
            showTooltip: false,
            width: 30,
            value: 75,
            handleSize: 0,
            handleShape: "square",
          circleShape: "half-top",
            startAngle: 50,
            endAngle: "+50",
            value: 50,
            create: function (v) {
                console.log('Create');
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
            }
        });

    },
    listenEvents: function () {
        var self = this;

        var cameraHandle = document.getElementById('camera_left_right');

        cameraHandle.addEventListener('change', function (ev) {
            self.data.command = 'camera';
            self.data.camera_left_right = this.value;
            self.send();
        });


        var cameraHandleUp = document.getElementById('camera_up_down');

        cameraHandleUp.addEventListener('change', function (ev) {
            self.data.command = 'camera';
            self.data.camera_up_down = this.value;
            self.send();
        });


        var sliderHandle = document.getElementsByClassName('rs-handle');

        sliderHandle[0].addEventListener('mousedown', function (ev) {
            self.data.command = 'forward';
            self.send();
        });

        sliderHandle[0].addEventListener('mouseup', function (ev) {
            self.data.command = 'stop';
            self.send();
        });

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

        request.open('GET',
            '/command?command=' + this.data.command +
            '&direction=' + this.data.direction +
            '&speed=' + this.data.speed +
            '&camera_left_right=' + this.data.camera_left_right +
            '&camera_up_down=' + this.data.camera_up_down +
            '&turning_angle=' + this.data.turning_angle

        );
        request.send();
    }
}



document.addEventListener('DOMContentLoaded', function () {

    carcontroller = new carController();
});