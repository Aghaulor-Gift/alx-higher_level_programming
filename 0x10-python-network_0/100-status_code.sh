#!/bin/bash
# script that sends a request to a URL & displays only the status code
curl -s -o /dev/null -w "%{http_code}" $1
