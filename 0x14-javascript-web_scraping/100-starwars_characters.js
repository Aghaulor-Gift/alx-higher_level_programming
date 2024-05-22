#!/usr/bin/node
// A script that retrieves and prints the names of all Star Wars characters from the Star Wars API.

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body);
  const data = films.characters;
  for (const idx of data) {
    request.get(idx, function (error, response, body1) {
      if (error) {
        console.error(error);
      }
      const films1 = JSON.parse(body1);
      console.log(films1.name);
    });
  }
});
