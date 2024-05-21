#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];
const userId = parseInt(process.argv[3]);

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  if (response.statusCode === 200) {
    if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    for (const userId in completedTasks) {
      console.log(`${userId}: ${completedTasks[userId]}`);
    }
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
  }
});
