#!/bin/bash
# Sends a DELETE request to the URL passed as first argument,& displays body
curl -sX DELETE "$1"
