#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}

    response = requests.post(url, data=data)
    json_data = response.json()

    if not q:
        print('q=""')

    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        if not response.text:
            print('Not a valid JSON')
        else:
            print('No result')
