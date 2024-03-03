#!/usr/bin/node
/*
Script stores an api response to a file
Takes in two arguments:
    the URI
    the filename
*/

const request = require('request');
const fs = require('fs');
const { error } = require('console');
const URL = process.argv[2];
const filename = process.argv[3];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    
  }
});
