import urllib2
import json
import requests

class get_images:

  def get_img(self, lat, lng):
      query_i= "https://api.foursquare.com/v2/venues/43695300f964a5208c291fe3/photos?oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170902"
      obj = urllib2.urlopen(query_i)
      data = json.load(obj)
      arr = data["response"]["photos"]["items"]
      arrer = []
      for i in arr:
          arrer.append(i["prefix"]+"height300"+i["suffix"])

      return arrergithub