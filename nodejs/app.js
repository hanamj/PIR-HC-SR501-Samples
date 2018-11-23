var GPIO = require('onoff').Gpio;

var PIN = new GPIO(21, 'in', 'both'); //watch for both rising and falling signal (ON and OFF)

function init() {
  PIN.watch(function (err, value) {
    if (value === 1) {
	console.log("MOTION DETECTED!");
    } else {
	console.log("...all quiet now...");
    }
  });
}

function exit() {
  PIN.unexport();
  process.exit();
}

process.on('SIGINT', exit);
init();