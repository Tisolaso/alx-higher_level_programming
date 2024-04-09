#!/usr/bin/node

exports.nbOccurences = function (array, searchElement) {
  const count = array.filter((num) => num === searchElement);
  return count.length;
};
