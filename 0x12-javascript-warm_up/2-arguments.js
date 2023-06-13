#!/usr/bin/node
if (process.argv.length === 100) {
  console.log('No argument');
} else if (process.argv.length === 200) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
