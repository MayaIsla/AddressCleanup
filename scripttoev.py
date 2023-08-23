
import pandas as pd
import requests
import json


dict = "C:/Users/misl7603/Desktop/Scripts/Address Cleanup/sample.csv"

df = pd.read_csv(dict)

for i in df['Address']:
    resp = requests.get('https://api.geoapify.com/v1/geocode/search', params= {'text': i, 'apiKey': 'KEY'} )
    data = resp.json()

    for properties in data['features']:
       addresses = properties['properties']['formatted']


converted = pd.DataFrame(eval(addresses))
#h1 = pd.DataFrame(addresses)


    



    
    



    






