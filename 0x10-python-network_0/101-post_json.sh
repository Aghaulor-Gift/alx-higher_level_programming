#!/bin/bash
# Script that sends a JSON POST request to a URL, and displays body 
curl -si -X POST -H "Content-Type: application/json" -d "@$2" "$1"
