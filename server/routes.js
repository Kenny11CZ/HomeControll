var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  	res.render('index', { title: 'Express' });
});
router.get('/statistics', function(req, res, next) {
	var fs = require("fs");
	fs.readFile('public/temperatures.txt', function (err, data) {
	   	if (err) {
	       	return console.error(err);
	    	res.render('statistics', {data: ""});
	   	}
	   	var json = "{}";
	   	try{
			json = JSON.parse(data.toString());
	   	}
	   	catch(e){}
	   	res.render('statistics', {data: JSON.parse(data.toString())});
	});
});
router.use("/public", express.static('public'));

module.exports = router;
