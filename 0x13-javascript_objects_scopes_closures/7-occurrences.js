#!/usr/bin/node

/* Script counts the number of occurrences of an element in a list */

exports.nbOccurences = function (list, searchElement) {
  if (! list || list.length === 0 || ! searchElement) {
    return 0;
  }
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
        count++;
    }
  }
}
