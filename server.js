let express = require('express');
let bodyParser = require('body-parser');

let api = require("./server/routes/api.routes");

let app = express();

//parse application/json
app.use(bodyParser.json({ type: 'application/json'}));

app.use("/api", api);
app.get('/', function (req, res) {
  res.send('Usage info goes here.');
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
})
