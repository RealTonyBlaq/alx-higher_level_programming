#!/usr/bin/node

/* Script computes the factorial of the number passed */

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log(1);
} else if (arg >= 1) {
  console.log(factorial(arg));
}
