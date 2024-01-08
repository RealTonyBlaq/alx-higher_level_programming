#!/usr/bin/node

/* Script prints the first argument passed to it */

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
