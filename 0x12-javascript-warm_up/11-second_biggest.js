#!/usr/bin/node
const args = process.argv.slice(2);
const sorted = args.slice(0);

if (args.length >= 2) {
  sorted.sort((a, b) => b - a);
  console.log(sorted[1]);
} else {
  console.log(0);
}
