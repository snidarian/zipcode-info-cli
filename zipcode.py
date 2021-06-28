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
    'ca' : ['Canada', 'AOA:Y1A', '1621'],
    'ch' : ['Switzerland', '1000:9658', '4614'],
    'cz' : ['Czech Republic', '100 00:798 62', '15507'],
    'de' : ['Germany', '01067:99998', '16482'],
    'dk' : ['Denmark', '0800:9990', '1182'],
    'do' : ['Dominican Republic', '10101:11906', '546'],
    'es' : ['Spain', '01001:52080', '56542'],
    'fi' : ['Finland', '00002:99999', '4637'],
    'fo' : ['Faroe Islands', '100:970', '130'],
    'fr' : ['France', '01000:98799', '51129'],
    'gb' : ['Great Britain', 'AB1:ZE3', '27769'],
    'gf' : ['French Guyana', '97300:97390', '25'],
    'gg' : ['Guernsey', 'GY1:GY9', '8'],
    'gl' : ['Greenland', '2412:3992', '33'],
    'gp' : ['Guadeloupe', '97100:97190', '33'],
    'gt' : ['Guatemala', '01001:22027', '548'],
    'gu' : ['Guam', '96910:96932', '23'],
    'gy' : ['Guyana', '97312:97360', '9'],
    'hr' : ['Croatia', '10000:53296', '6943'],
    'hu' : ['Hungary', '1011:9985', '4041'],
    'im' : ['Isle of Man', 'IM1:IM9', '86'],
    'in' : ['India', '110001:855126', '15226'],
    'is' : ['Iceland', '101:902', '148'],
    'it' : ['Italy', '00010:98168', '19940'],
    'je' : ['Jersey', 'JE1:JE3', '4'],
    'jp' : ['Japan', '100-0001:999-8531', '94388'],
    'li' : ['Liechtenstein', '9485:9498', '13'],
    'lk' : ['Sri Lanka', '*:96167', '1832'],
    'lt' : ['Lithuania', '00001:99069', '20558'],
    'lu' : ['Luxembourg', 'L-1009:L-9999', '4334'],
    'mc' : ['Monaco', '98000:98000', '29'],
    'md' : ['Moldavia', 'MD-2000:MD7731', '1753'],
    'mh' : ['Marshall Islands', '96960:96970', '2'],
    'mk' : ['Macedonia', '1000', '7550'],
    'mp' : ['Northern Mariana Islands', '', '4'],
    'mq' : ['Martinique', '', '34'],
    'mx' : ['Mexico', '', ''],
    'my' : ['Malasia', '', ''],
    'nl' : ['Holland', '', ''],
    'no' : ['Norway', '', ''],
    'nz' : ['New Zealand', '', ''],
    'ph' : ['Phillippines', '', ''],
    'pk' : ['Pakistan', '', ''],
    'pl' : ['Poland', '', ''],
    'pm' : ['Saint Pierre and Miquelon', '', ''],
    'pr' : ['Puerto Rico', '', ''],
    'pt' : ['Portugal', '', ''],
    're' : ['French Reunion', '', ''],
    'ru' : ['Russia', '101000:901993', '43538'],
    'se' : ['Sweden', '10005:98499', '16079'],
    'si' : ['Slovenia', '1000:9600', '557'],
    'sj' : ['Svalbard & Jan Mayen Islands', '8099:9178', '8'],
    'sk' : ['Slovak Republic', '010 01:992 01', '4152'],
    'sm' : ['San Marino', '47890:47899', '26'],
    'th' : ['Thailand', '10100:96220', '902'],
    'tr' : ['Turkey', '01000:81950', '51379'],
    'us' : ['United States', '00210:99950', '43624'],
    'va' : ['Vatican', '00120:00120', '2'],
    'vi' : ['Virgina Islands', '00801:00851', '16'],
    'yt' : ['Mayotte', '97600:97680', '17'],
    'za' : ['South Africa', '0002:9992', '3920'],
    
    }



# Aquire json string response from Web API
get_request_results = requests.get(f"https://api.zippopotam.us/{args.country}/{args.zipcode}")


# Change from json string to python dictionary
json_payload = get_request_results.json()


print(json_payload)
































