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
      const userID = dict.userID
      let taskCount = 0;
      for (const d of data) {
        if (d.userId === userID && d.completed === true) {
          
        }
      }
    }
  }
})
