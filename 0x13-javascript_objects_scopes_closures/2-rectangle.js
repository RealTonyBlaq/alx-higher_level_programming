#!/usr/bin/node

/* Script creates a class that defines a rectangle */

class Rectangle {
  /*
  Defines the class Rectangle

  if w or h is <= 0, an empty class is created.
  */
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
