const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter marks: ", function (m) {
    if (m >= 40) {
        console.log("Pass");
    } else {
        console.log("Fail");
    }
    rl.close();
});