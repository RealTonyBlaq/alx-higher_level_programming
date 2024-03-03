#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
    "Return of the Jedi"
*/

const request = require('request');
const movieID = process.argv[2];
const filmURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
const peopleURL = 'https://swapi-api.alx-tools.com/api/people/';

request.get(filmURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const personURL of characters)
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
    };
  }
});
