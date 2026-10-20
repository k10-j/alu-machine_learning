#!/usr/bin/env python3
"""Return home planet names of all sentient species."""

import requests


def sentientPlanets():
    """Return a list of home planets of sentient species."""
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for species in data["results"]:
            classification = species["classification"]
            designation = species["designation"]

            if (classification == "sentient" or
                    designation == "sentient"):
                homeworld = species["homeworld"]

                if homeworld:
                    planet_response = requests.get(homeworld)
                    planet_response.raise_for_status()
                    planet = planet_response.json()
                    planets.append(planet["name"])

        url = data["next"]

    return planets