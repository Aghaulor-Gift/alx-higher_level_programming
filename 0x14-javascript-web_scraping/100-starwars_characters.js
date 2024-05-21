#!/usr/bin/node
// A script that retrieves and prints the names of all Star Wars characters from the Star Wars API.

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const character = JSON.parse(body).results;
    console.log('Star Wars Characters:');
    character.forEach(characters => {
      console.log(characters.name);
    });
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
