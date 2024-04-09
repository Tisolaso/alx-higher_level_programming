#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square extends Square {
  charPrint (c = 'X') {
    let line = '';

    for (let i = 0; i < this.width; i++) {
      line += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
};
