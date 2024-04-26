#!/usr/bin/python3
""" A module that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
