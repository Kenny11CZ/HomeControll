var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  	res.render('index', { title: 'Express' });
});
router.get('/statistics', function(req, res, next) {
	var fs = require("fs");
	fs.readFile('temperatures.txt', function (err, data) {
	   if (err) {
	       return console.error(err);
	       res.render('statistics', {data: ""});
	   }
	   console.log("Asynchronous read: " + data.toString());
	   res.render('statistics', {data: data.toString()});
	});
});

module.exports = router;
