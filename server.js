let express = require("express");
let bodyParser = require("body-parser");

let api = require("./server/routes/api.routes");

let app = express();

//parse application/json
app.use(bodyParser.json({ type: "application/json"}));

// serve API routes
app.use("/api", api);

// serve static files
app.use(express.static("public"));



app.listen(3000, function () {
  console.log("TTR Server listening on port 3000!");
});
