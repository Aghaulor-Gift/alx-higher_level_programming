#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode
// number matches a given integer.

const request = require('request');
const movie_Id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:movie_Id';

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
