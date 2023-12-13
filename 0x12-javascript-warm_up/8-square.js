#!/usr/bin/node
/* Script prints a square for args using X */

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    for (let k = 0; k < size; k++) {
        console.log('X', "");
    }
    i++;
  }
} else {
    console.log('Missing size');
}
