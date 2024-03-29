#!/usr/bin/node
/*
Script prints the number of movies where
the character “Wedge Antilles” is present
*/

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    for (const dict of data.results) {
      for (const character of dict.characters) {
        const value = character.split('/');
        const id = Number(value[value.length - 2]);
        if (id === 18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
