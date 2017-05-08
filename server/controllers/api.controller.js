const longestBridge = require('../python/longest_bridge.js');

var Controller = function() {


  function longest(req, res) {
    if (!req.body.routes) {
      return res.status(403).json(req.body).end();
    }

    // TODO add error handling to longestBridge and this
    longestBridge(req.body, function (data) {
      // if (err) return res.status(500).send(err);
      return res.json(data);
    });
  }

  return {
    longest
  };
}();

module.exports = Controller;
