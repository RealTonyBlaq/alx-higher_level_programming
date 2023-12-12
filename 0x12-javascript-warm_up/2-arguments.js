#!/usr/bin/node
/* Script to check if arguments were passed to the script */
const argsCount = process.argv.length - 2;
if (argsCount === 1) {
  console.log('Argument found');
} else if (argsCount > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
