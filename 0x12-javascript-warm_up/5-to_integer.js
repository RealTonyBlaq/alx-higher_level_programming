#!/usr/bin/node

/* Script checks if an argument is a number */

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number:', arg);
}
