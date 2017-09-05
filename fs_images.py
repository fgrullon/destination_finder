from urllib.request import urlopen
import json
import requests

class get_images:

  def get_img(self, lat, lng):
    client_id = "WBAHTTWXR1GU0KIROJN1RT333EST1Q05TYHQ4XYB14VNO134"
    client_secret = "OB4UGDBJ5JBTQKFKRKPCFFGSS5Z2EPTUO4POC41LWQYPEIF1"
    location = "{0},{1}".format(lat, lng)
    api = "https://api.foursquare.com/v2/venues/search?client_id="+client_id+"&client_secret="+client_secret+"&v=20130815&ll=18.48,-69.93"
    ex = "https://api.foursquare.com/v2/venues/explore?ll="+location+"&oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170904&radius=250"
    query = "https://api.foursquare.com/v2/venues/explore?ll=18.4,-69&radius=250&oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170905"
    query_last = "https://api.foursquare.com/v2/venues/explore?ll=18.48,-69.93&radius=250&oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170905"
    obj = urlopen(api)
    data = json.load(obj)
    result = data["response"]["venues"]
    for key in result:
      print("{}".format(key))
      #print("Result : {}\n".format(key["items"][i]["venue"]["name"]))

    #key["items"][0]["venue"]["name"]
"""
  	name = name.replace(" ", "")
  	#Get the venue id
  	query_id = "https://api.foursquare.com/v2/venues/search?query="+name+"&intent=global&oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170904"
  	
  	obj_id = urlopen(query_id)
  	data_id = json.load(obj_id)
  	venue_id = data_id["response"]["venues"][0]["id"]
  	print(data_id["response"]["venues"][0])

  	#Using the venue id we search for images of the place
  	query_img= "https://api.foursquare.com/v2/venues/"+venue_id+"/photos?oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170902"
  	obj_img = urlopen(query_img)
  	data_img = json.load(obj_img)

  	images = data_img["response"]["photos"]["items"]
  	arrer = []
  	for i in images:
  		arrer.append(i["prefix"]+"height300"+i["suffix"])

  	return arrer 

"""