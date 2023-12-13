#!/usr/bin/node
/* Script prints a square for args using X */

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
} else {
  console.log('Missing size');
}
