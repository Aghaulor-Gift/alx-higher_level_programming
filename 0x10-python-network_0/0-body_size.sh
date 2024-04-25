#!/bin/bash
# script that sends a request to that URL, and displays the size.
curl -sI "$1" | grep -i 'content-length'| awk '{print "$2"}'
