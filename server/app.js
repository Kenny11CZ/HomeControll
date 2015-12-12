
var express = require('express');
var routes = require('./routes.js')
var app = express();
app.set('view engine', 'jade');
app.use('/', routes);


var server = app.listen(80, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
