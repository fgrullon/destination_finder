from urllib.request import urlopen
import json
import requests

class get_images:

  def get_catg(self):
    quer = "https://api.foursquare.com/v2/venues/categories?oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170913"
    obj_id = urlopen(quer)
    data_id = json.load(obj_id)
    for cat in data_id['response']['categories']:
        print("Cat: {0}, Id: {1}".format(cat['name'],cat['id'])) 

  def get_venue_id(self, lat, lng):
    client_id = "WBAHTTWXR1GU0KIROJN1RT333EST1Q05TYHQ4XYB14VNO134"
    client_secret = "OB4UGDBJ5JBTQKFKRKPCFFGSS5Z2EPTUO4POC41LWQYPEIF1"
    token = "OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4"
    location = "{0:.2f},{1:.2f}".format(lat,lng)
    query_id = "https://api.foursquare.com/v2/venues/search?ll="+location+"&categoryId=4d4b7104d754a06370d81259&oauth_token="+token+"&v=20170904"
    obj_id = urlopen(query_id)
    data_id = json.load(obj_id)
    venues = data_id['response']['venues']
    images = []
    for item in venues:
        result = self.get_img(item['id'])
        if result != None:
            images.append(result)
    return images



  def get_img(self, venue_id):
    client_id = "WBAHTTWXR1GU0KIROJN1RT333EST1Q05TYHQ4XYB14VNO134"
    client_secret = "OB4UGDBJ5JBTQKFKRKPCFFGSS5Z2EPTUO4POC41LWQYPEIF1" 
    query_img= "https://api.foursquare.com/v2/venues/"+venue_id+"/photos?client_id="+client_id+"&client_secret="+client_secret+"&v=20170904"
    obj_img = urlopen(query_img)
    data_img = json.load(obj_img)
    images = data_img["response"]["photos"]["items"]
    arrer = []
    if len(images) > 0:
      return images[0]["prefix"]+"300x300"+images[0]["suffix"]

