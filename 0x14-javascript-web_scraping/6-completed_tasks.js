#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const idx in tasks) {
      const task = tasks[idx];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
