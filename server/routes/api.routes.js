var Controller = require("../controllers/api.controller");

var express = require("express");
var Router = express.Router;

var router = new Router();

// compute longest path
router.route("/longest").post(Controller.longest);

module.exports = router;
