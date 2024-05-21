#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode
// number matches a given integer.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
