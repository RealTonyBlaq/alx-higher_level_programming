#!/usr/bin/node
/*
Script computes the number of tasks completed by user id
Accepts one argument:
    The API URI
*/

const request = require('request');
const URI = process.argv[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    data = JSON.parse(body);
    tasks = {};
    for (const dict of data) {
      userID = dict.userID
      for (d of data) {

      }
    }
  }
})
