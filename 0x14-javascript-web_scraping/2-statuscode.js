#!/usr/bin/node
/* Script displays the status code of a GET request */

const req = require('request');
const URL = process.argv[2];

const statusCode = req.get(URL)

