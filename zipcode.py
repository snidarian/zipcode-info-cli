#!/usr/bin/python3

# queries web api to acquire information on supplied zip code


import requests
import argparse


# set up argparse
parser = argparse.ArgumentParser(description="supply zip code argument to get information about the zipcode")

args = parser.add_argument("Zipcode", help="zip code argument", type=str)

args = parser.parse_args()

# 
get_request_results = requests.get("https://api.zippopotam.us/us/90210")

json_payload = get_request_results.json()


print(json_payload)
































