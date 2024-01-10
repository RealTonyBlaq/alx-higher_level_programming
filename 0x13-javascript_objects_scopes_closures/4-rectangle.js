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

  print () {
    if (this.width >= 1 && this.height >= 1) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    /* method exchanges the values of width and height */
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    /* method doubles the value of the attributes */
    if (this.height >= 1 && this.width >= 1) {
      this.height *= 2;
      this.width *= 2;
    }
  }
}

module.exports = Rectangle;
