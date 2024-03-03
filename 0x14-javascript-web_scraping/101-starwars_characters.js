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
    const charactersList = [];

    const fetchCharacterDetails = (character) => {
      const list = character.split('/');
      const id = list[list.length - 2];

      request.get(peopleURL + `${id}`, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }
        if (response.statusCode === 200) {
          const person = JSON.parse(body);
          charactersList.push(person.name);

          if (charactersList.length === data.characters.length) {
            charactersList.forEach((elem) => console.log(elem));
          }
        }
      });
    };


    data.characters.forEach(fetchCharacterDetails);
  }
});