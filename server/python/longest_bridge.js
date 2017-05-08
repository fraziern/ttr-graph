function longestBridge(json, cb) {
  var spawn = require('child_process').spawn;

  // since the python scripts aren't at root, must use __dirname
  var py = spawn('python', ['longest_stdout.py'], {cwd: __dirname});
  var dataOutput = '';

  py.stdout.on('data', (data) => {
    dataOutput = data.toString();
  });
  py.stdout.on('end', () => {
    // console.log(`dataOutput: ${dataOutput}`);
    cb(JSON.parse(dataOutput));
  });
  py.on('error', (err) => {
    console.log('Error in python spawn: ' + err);
  });

  // Handle error output
  py.stderr.on('data', (data) => {
    console.log(data.toString());
  });

  py.on('exit', (code) => {
    console.log("Spawn process quit with code: " + code);
  });

  py.stdin.write(JSON.stringify(json));
  py.stdin.end();
}

module.exports = longestBridge;
