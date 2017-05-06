function longestBridge(json, cb) {
  var spawn = require('child_process').spawn;
  var py = spawn('python', ['longest_stdout.py']);
  var dataOutput = '';

  py.stdout.on('data', function(data) {
    dataOutput = data.toString();
  });
  py.stdout.on('end', function() {
    // console.log(`dataOutput: ${dataOutput}`);
    cb(dataOutput);
  });

  py.stdin.write(JSON.stringify(json));
  py.stdin.end();
}

module.exports = longestBridge;
