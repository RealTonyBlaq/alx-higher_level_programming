#!/usr/bin/node
/* Script prints the first argument passed to it */
const argsCount = process.argv.length - 2;
if (argsCount === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
