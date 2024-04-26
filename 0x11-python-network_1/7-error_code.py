#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    x = requests.get(url)
    print(x.text)

    if (x.status_code >= 400):
        print('Error code: ', x.status_code)
