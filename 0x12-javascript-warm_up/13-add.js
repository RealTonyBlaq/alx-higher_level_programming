#!/usr/bin/node
/*
Script creates a function "add" that is visible from outside
which means it can be imported by another script
*/

function add(a, b) {
  return a + b;
}

module.exports = {
  add
};
