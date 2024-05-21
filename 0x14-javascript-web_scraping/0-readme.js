#!/usr/bin/node
/*  read and write a file using fs module */
const fs = require('fs');

/* Read The first argument is the file path */
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    /* If an error occurred during the reading, print the error object */
    return console.log(err);
  }
  process.stdout.write(data);
});
