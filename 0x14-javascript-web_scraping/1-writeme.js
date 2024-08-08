#!/usr/bin/node
/* Script writes a string to a file */

const fs = require('fs');
const path = require('path');

const file = process.argv[2];
const content = process.argv[3];

if (!file || !content) {
  console.error('Usage: ./script.js <file> <content>');
  process.exit(1);
}

// Ensure directory exists
const dir = path.dirname(file);
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

fs.writeFile(file, content, 'utf-8', (err) => {
  if (err) {
    console.error(`Error writing to file: ${err.message}`);
    process.exit(1);
  }
  console.log('File written successfully');
});
