#!/bin/bash
# Request to 0.0.0.0:5000/catch_me & the server get a response You got me!
curl -s -X POST -d "You got me!" 0.0.0.0:5000/catch_me
