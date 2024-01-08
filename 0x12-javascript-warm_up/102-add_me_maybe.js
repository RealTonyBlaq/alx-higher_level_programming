#!/usr/bin/node

/* Script increments and calls a function */

exports.addMeMaybe = function (number, func) {
  number++;
  func(number);
}
