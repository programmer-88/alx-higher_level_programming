#!/usr/bin/node

const argsCount = process.argv.length;
console.log(argsCount === 2 ? 'No argument' : argsCount === 3 ? 'Argument found' : 'Arguments found');
