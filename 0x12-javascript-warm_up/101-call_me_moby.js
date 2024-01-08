#!/usr/bin/node

/* Script executes a function x times using another function */

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
