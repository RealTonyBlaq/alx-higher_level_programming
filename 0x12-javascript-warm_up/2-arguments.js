#!/usr/bin/node

/* Script prints a string if an argument was passed to it */

const arg = process.argv.length - 2;
if (arg === 0) {
  console.log('No argument');
} else if (arg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
