var express = require('express');

var api = require("./server/routes/api.routes");

var app = express();

app.get('/', function (req, res) {
  res.send('Usage info goes here.');
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
})
