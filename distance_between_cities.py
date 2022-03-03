import urllib.parse
from urllib.request import urlopen
import json, ssl, numpy as np, haversine, html.parser
from bs4 import BeautifulSoup


API_KEY = 'pk.eyJ1Ijoic2ViYXNncmFjaWEiLCJhIjoiY2wwYmMwczR2MGkxYjNlbWlocDNtc3JrOCJ9.CuzZJ_4lHNxVSdkUR928cw'
ssl._create_default_https_context = ssl._create_unverified_context

def get_city_coords(city):

    city_coords = {'latitude': 0, 'longitude': 0}
    url_city = "https://api.mapbox.com/geocoding/v5/mapbox.places/"+ city +".json?access_token=" + API_KEY
    response = urlopen(url_city)
    data_json = json.loads(response.read())
    data_json.keys()
    city_coords['latitude'] = data_json['features'][0]['center'][0]
    city_coords['longitude'] = data_json['features'][0]['center'][1]
    return city_coords

def haversine_algo(lat1, lat2, lon1, lon2):
    # https://stackoverflow.com/questions/29545704/fast-haversine-approximation-python-pandas
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


if __name__ == '__main__':

    from_city = input('Type your first city: ')#.replace(' ', '%20' )
    to_city = input('Type your second city: ')#.replace(' ', '%20' )

    from_city_parsed = urllib.parse.quote(from_city)
    to_city_parsed = urllib.parse.quote(to_city)

    city_one = {'latitude': 0, 'longitude': 0}
    city_two = {'latitude': 0, 'longitude': 0}

    try:
        city_one = get_city_coords(from_city)
    except:
        print(f'Could not get coordinates for: {from_city}')
    finally:
        print(f'Coordinates found for city {from_city_parsed}: {city_one}')

    try:
            city_two = get_city_coords(to_city)
    except:
        print(f'Could not get coordinates for: {to_city}')
    finally:
        print(f'Coordinates found for city {to_city_parsed}: {city_two}')


    print('\n')
    print('Answer in Kilometers:')
    # Using Haversine module
    print(haversine.haversine((city_one['latitude'], city_one['longitude']), (city_two['latitude'], city_two['longitude'])))
    # Using Haversine algo from the internet
    print(haversine_algo(city_one['latitude'], city_two['latitude'], city_one['longitude'], city_two['longitude']))

    print('\n')
    print('Answer in Miles:')
    # Using Haversine module
    print(haversine.haversine((city_one['latitude'], city_one['longitude']), (city_two['latitude'], city_two['longitude']), unit='mi'))
    # Using Haversine algo from the internet
    print(haversine_algo(city_one['latitude'], city_two['latitude'], city_one['longitude'], city_two['longitude']) * 0.621371)