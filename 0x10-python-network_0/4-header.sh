#!/bin/bash
# Script takes URL as an argument, sends a GET request, & displays the body
curl -s -H "X-School-User-Id: 98" "$1"
