#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(`${movie.title}:`);
    movie.characters.forEach(characterUrl => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error(charError);
          return;
        }
        if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.error(`Error: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
