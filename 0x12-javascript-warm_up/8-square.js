#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (!isNaN(number)) {
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
} else {
  console.log('Missing size');
}
