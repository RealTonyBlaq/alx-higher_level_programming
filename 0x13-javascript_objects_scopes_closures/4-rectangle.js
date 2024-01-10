#!/usr/bin/node

/* Script creates a class that defines a rectangle */

class Rectangle {
  /*
  Defines the class Rectangle

  if w or h is <= 0, an empty class is created.
  */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width >= 1 && this.height >= 1) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    /* method exchanges the values of width and height */
    if (this.height && this.width) {
      [this.height, this.width] = [this.width, this.height];
    }
  }

  double () {
    /* method doubles the value of the attributes */
    if (this.height && this.width) {
      this.height *= 2;
      this.width *= 2;
    }
  }
}

module.exports = Rectangle;
