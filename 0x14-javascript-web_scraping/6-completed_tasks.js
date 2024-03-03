#!/usr/bin/node
/*
Script computes the number of tasks completed by user id
Accepts one argument:
    The API URI
*/

const request = require('request');
const URI = process.argv[2];

request.get
