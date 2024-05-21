#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode
// number matches a given integer.

const request = require('request');
const movie_Id = process.arrgv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:movie_Id';
const film;
request(url, (error, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
