#!/usr/bin/node
/* Script reads content from a file */

const reader = require('fs')
const contents = reader.createReadStream(process.argv[1], )

