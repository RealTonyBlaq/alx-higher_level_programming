#!/usr/bin/node
/* Script reads content from a file */

const reader = require('fs');

reader.readFile(process.argv[2], 'utf-8', (err, contents) => {
  if (err) {
    console.error(err);
    return;
  } else {
    console.log(contents);
  }
});
