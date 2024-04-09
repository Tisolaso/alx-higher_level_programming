#!/usr/bin/node
const args = process.argv.slice(2);

let sum = 1;

function factorial(fact) {
  for (let i = 2; i <= fact; i++) {
    sum = i * sum;
  }
  console.log(sum);
}

factorial(parseInt(args[0]));

