#!/bin/bash
# script takes in a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -i "allow" | awk '{print "$2"}'
