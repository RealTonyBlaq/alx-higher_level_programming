#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
using the movie ID passed as an argument to this script
*/

const request = require('request');
const movieID = process.argv[2];
const filmURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(filmURL, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (const personURL of data.characters) {
      try {
        const personResponse = await new Promise((resolve, reject) => {
          request.get(personURL, (error, response, body) => {
            if (error) reject(error);
            else resolve({ response, body });
          });
        });
        if (personResponse.response.statusCode === 200) {
          const person = JSON.parse(personResponse.body);
          console.log(person.name);
        }
      } catch (err) {
        console.error(err);
      }
    }
  }
});
