#!/usr/bin/node

/* Script creates a class Sqaure that inherits another square */

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
