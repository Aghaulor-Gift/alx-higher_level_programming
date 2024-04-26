#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    headers = {
        "Authorization": "Basic " + f"{username}:{password}".encode(
            "ascii").hex()
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_id = response.json()["id"]
        print("Your GitHub user id is:", user_id)
    else:
        print("Error:", response.text)
