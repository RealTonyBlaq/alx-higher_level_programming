#!/usr/bin/node

/* Script prints a square using the letter 'x' */

const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else if (size >= 1) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
