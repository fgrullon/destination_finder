import urllib2
import json
import requests

class location:

  def get_lat_lng(self, name):
    params = {
        'address' : name,
        'sensor' : 'false'
        }
    query = "https://maps.googleapis.com/maps/api/geocode/json"
    req = requests.get(query, params=params)
    res = req.json()
    lat = res['results'][0]['geometry']['location']['lat']
    lng = res['results'][0]['geometry']['location']['long']
    return (lat, lng)

