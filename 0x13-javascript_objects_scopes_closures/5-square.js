#!/usr/bin/node

/* Script creates a class Square that inherits Rectangle */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }
}
