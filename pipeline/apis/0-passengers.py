#!/usr/bin/env python3
"""
Return a list of ships that can hold a given number of passengers.
"""

import requests


def availableShips(passengerCount):
    """Return ships with at least the requested passenger capacity."""
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")

            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])
            except ValueError:
                continue

        url = data.get("next")

    return ships