#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const item = 'X';
    let line = '';

    for (let i = 0; i < this.width; i++) {
      line += item;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate() {
    const num = this.width;
    this.width = this.height;
    this.height = num;
  }
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

