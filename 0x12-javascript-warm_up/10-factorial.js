#!/usr/bin/node
/* Script computes the factorial of the first argument passed */

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  if (n > 1) {
    factorial(n - 1);
}
