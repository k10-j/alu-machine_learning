#!/usr/bin/env python3
"""Script that prints the location of a specific user."""

import requests
import sys
import time


if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if response.status_code == 403:
        rate_limit = int(response.headers.get("X-RateLimit-Reset", 0))
        current_time = int(time.time())
        diff = (rate_limit - current_time) / 60
        print("Reset in {} min".format(int(diff)))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 200:
        data = response.json()
        print(data.get("location"))