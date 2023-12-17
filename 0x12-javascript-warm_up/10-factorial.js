#!/usr/bin/node
/* Script computes the factorial of the first argument passed */

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  if (n > 1) {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];

if (!isNaN(arg)) {
  console.log(factorial(arg));
} else {
  console.log(factorial(1));
}
