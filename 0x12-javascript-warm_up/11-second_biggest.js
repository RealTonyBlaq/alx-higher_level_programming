#!/usr/bin/node

/* Script searches for the second largest number in the list of arguments */

const argLength = process.argv.length - 2;
if (argLength <= 1) {
  console.log(0);
}
