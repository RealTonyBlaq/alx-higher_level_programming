#!/usr/bin/node

/* Script counts the number of occurrences of an element in a list */

exports.nbOccurences = function (list, searchElement) {
  if (!list || list.length === 0 || !searchElement) {
    return 0;
  }
  const listFilter = list.filter(list => list === searchElement);
  return listFilter.length;
};
