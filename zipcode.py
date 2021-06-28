#!/usr/bin/python3

# queries web api to acquire information on supplied zip code


import requests
import argparse


# set up argparse
parser = argparse.ArgumentParser(description="supply zip code argument to get information about the zipcode")

args = parser.add_argument("zipcode", help="zip code argument", type=str)
args = parser.add_argument('-', '--country', help='', type=str, default='us')
args = parser.add_argument('-ls', '--list-countries', help='list country abbreviations')

args = parser.parse_args()


country_abbreviations = { 
    'ad' : 'Andorra',
    'ar' : 'Argentina',
    'as' : 'American Samoa',
    'at' : 'Austria',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',
    '' : '',


    }



# Aquire json string response from Web API
get_request_results = requests.get(f"https://api.zippopotam.us/{args.country}/{args.zipcode}")


# Change from json string to python dictionary
json_payload = get_request_results.json()


print(json_payload)
































