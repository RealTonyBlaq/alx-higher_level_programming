#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
using the movie ID passed as an argument to this script
*/

const request = require('request');
const movieID = process.argv[2];
const filmURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(filmURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const personURL of data.characters) {
      request.get(personURL, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }
        if (response.statusCode === 200) {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
