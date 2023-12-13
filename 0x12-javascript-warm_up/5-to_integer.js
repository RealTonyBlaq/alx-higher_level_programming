#!/usr/bin/node
/* Script converts args to integers */
if (type(Process.argv[2]) === Number) {
  console.log('My number: ', process.argv[2]);
} else {
  console.log('Not a number');
}
