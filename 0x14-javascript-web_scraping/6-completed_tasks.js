#!/usr/bin/node
/*
Script computes the number of tasks completed by user id
Accepts one argument:
    The API URI
*/

const request = require('request');
const URI = process.argv[2];

request.get(URI, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    
    // Using reduce to count completed tasks for each user
    const tasks = data.reduce((acc, task) => {
      const userID = task.userId;
      if (task.completed === true) {
        acc[userID] = (acc[userID] || 0) + 1;
      }
      return acc;
    }, {});

    console.log(tasks);
  }
});
