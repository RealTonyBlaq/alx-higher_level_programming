#!/usr/bin/node
/*
Script prints the title of a Star Wars movie
where the episode number matches a given integer
*/

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/:id';

request.get()
