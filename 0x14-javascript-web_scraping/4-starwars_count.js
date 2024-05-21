#!/usr/bin/node
// A  script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const apiUrl = process.argv[2];
const charID = '18';
const charUrl = `https://swapi-api.alx-tools.com/api/people/${charID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(charUrl)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
