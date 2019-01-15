var http = require('http');
const i2c = require('i2c-bus');

http.createServer(function (req, res) {

    
    res.write('Pie');
    res.end();





}).listen(8090);