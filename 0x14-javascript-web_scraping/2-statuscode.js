#!/usr/bin/node
/* Script displays the status code of a GET request */

const { error } = require('console');
const req = require('request');
const URL = process.argv[2];

req.get(URL, (error, response) => {
  if (error) {
    console.errror(error)
    return;
  }
  console.log('code:', response.statusCode)
});
