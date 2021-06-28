#!/usr/bin/python3

# queries web api to acquire information on supplied zip code


import requests
import argparse


# set up argparse
parser = argparse.ArgumentParser(description="supply zip code argument to get information about the zipcode")

args = parser.add_argument("zipcode", help="zip code argument", type=str)
args = parser.add_argument('-c', '--country', help='specify country abbrev', type=str, default='us')
args = parser.add_argument('-ls', '--list-countries', help='list country abbreviations')

args = parser.parse_args()


country_abbreviations = { 
    'ad' : ['Andorra', 'AD100:AD700', '7'],
    'ar' : ['Argentina', '1601:9431', '20260'],
    'as' : ['American Samoa', '96799:96799', '1'],
    'at' : ['Austria', '1010:9992', '4877'],
    'au' : ['Australia', '0200:9726', '101161'],
    'bd' : ['Bangladesh', '1000:9461', '1323'],
    'be' : ['Belgium', '1000:9992', '3386'],
    'bg' : ['Bulgaria', '1000:9974', '5304'],
    'br' : ['Brazil', '01000-000:99990-000', '5526'],
    }



# Aquire json string response from Web API
get_request_results = requests.get(f"https://api.zippopotam.us/{args.country}/{args.zipcode}")


# Change from json string to python dictionary
json_payload = get_request_results.json()


print(json_payload)
































