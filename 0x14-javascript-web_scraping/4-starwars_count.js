#!/usr/bin/node
/*
Script prints the number of movies where
the character “Wedge Antilles” is present
*/

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    data = JSON.parse(body);
    console.log(data);
  }
});
