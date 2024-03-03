#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
    "Return of the Jedi"
*/

const request = require('request');
const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;


