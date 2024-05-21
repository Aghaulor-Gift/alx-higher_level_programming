#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  if (response.statusCode === 200) {
    try {
      fs.writeFileSync(filePath, body, 'utf-8');
    } catch (writeErr) {
      console.error(writeErr);
    }
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
