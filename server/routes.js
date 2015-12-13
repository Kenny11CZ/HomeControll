var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  	res.render('inde', { title: 'Express' });
});
router.get('/statistics', function(req, res, next) {
	var fs = require("fs");
	fs.readFile('temperatures.txt', function (err, data) {
	   if (err) {
	       return console.error(err);
	       res.render('statistics', {data: ""});
	   }
	   res.render('statistics', {data: JSON.parse(data.toString())});
	});
});
router.use("/public", express.static('public'));

module.exports = router;
