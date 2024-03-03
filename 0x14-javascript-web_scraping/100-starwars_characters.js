#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
    "Return of the Jedi"
*/

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(URL, (error, response, body) => {
 if (error) {
    console.error(error);
    return;
 }
 if (response.statusCode === 200) {
    const data = JSON.parse(body)
    for (const character of data.characters) {
      const list = character.split('/');
      const person = list[list.length - 2];
    }
 }
})
