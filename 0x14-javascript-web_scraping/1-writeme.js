#!/usr/bin/node
/* Script writes a string to a file */

const writer = require('fs');
const file = process.argv[2];
const content = process.argv[3]

writer.writeFile(file, content, 'utf-8',)
