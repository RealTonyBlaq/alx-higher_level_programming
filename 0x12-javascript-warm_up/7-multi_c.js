#!/usr/bin/node

/* Script prints a string a number of times */

const count = Number(process.argv[2]);
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else if (count >= 1) {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
