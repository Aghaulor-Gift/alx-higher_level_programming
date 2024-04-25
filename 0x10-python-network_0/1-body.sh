#!/bin/bash
# script takes in a URL, sends a GET request to the URL, and displays the body
curl -s -w "%{http_code}" -o /dev/null "$1" | grep -q '200' && curl -s "$1"
