#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const index = 0;
    printCharacters(characters, index);
  } else {
    console.error('Error:', error);
  }
});

function printCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error:', error);
      }
    });
  }
}
