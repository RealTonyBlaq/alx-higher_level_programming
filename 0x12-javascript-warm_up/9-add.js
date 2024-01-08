#!/usr/bin/node

/* Script adds to numbers passed to it */

function add (a, b) {
  return (a + b);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
console.log(add(a, b));
