#!/usr/bin/node
/*
Script prints the title of a Star Wars movie
where the episode number matches a given integer
*/

const request = require('request');
const id = 
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request.get(URL, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  data = response.toJSON();
  console.log(data.title);
});