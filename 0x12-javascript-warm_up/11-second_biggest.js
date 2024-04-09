#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount < 2) {
  console.log(0);
} else {
  
  const args = process.argv.slice(2).map(arg => parseInt(arg));
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
