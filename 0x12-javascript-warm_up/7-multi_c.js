#!/usr/bin/node
/*
Script prints x number of times a string, x is defined
by the first argument passed to the script
*/
const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
