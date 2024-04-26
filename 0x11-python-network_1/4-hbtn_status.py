#!/usr/bin/bash
""" script that fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    x = requests.get(url)
    data = x.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
