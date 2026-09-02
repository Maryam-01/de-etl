# ADD YOUR IMPORTS HERE

import requests
import json
# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE

import requests

def get_simpsons_quote():
    r = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
    body = r.json()[0]
    return f"{body['character']}: {body['quote']}"


print(get_simpsons_quote())
