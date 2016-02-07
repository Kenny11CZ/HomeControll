
var express = require('express');
var routes = require('./routes.js')
var app = express();

var fs = require("fs");

app.set('views', __dirname + '/views')
app.set('view engine', 'jade');
app.use('/', routes);


var server = app.listen(80, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
var io = require('socket.io')(server, { log: true });
io.on('connection', function(client) {  
    console.log('Client connected...');

    client.on('join', function(data) {
        console.log(data);
    });
    var timer = "";
    fs.watchFile('temperatures.txt', {persistent:true, interval:1000}, 
    	function(data){
	    	timer = setTimeout(function(){
	    		io.sockets.emit('filechanged', ''); 
	    		console.log('filechanged');
	    	}, 1200);
	    });

});
