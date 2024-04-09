#!/usr/bin/node
const args = process.argv.slice(2);

const item = 'X';
const times = parseInt(args[0]);

if (!isNaN(args[0])) {
  for (let i = 1; i <= times; i++) {
    let line = '';
    for (let y = 1; y <= times; y++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}

