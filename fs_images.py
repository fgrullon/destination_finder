from urllib.request import urlopen
import json
import requests

class get_images:

  def get_img(self, lat, lng):
  	location = "{0},{1}".format(lat, lng)
  	ex = "https://api.foursquare.com/v2/venues/search?ll="+location+"&oauth_token=OWCWXKGK0CR1HSDG40Q4422IWUYB5PQW1YJKITQQJO5EBKE4&v=20170904"
  	obj = urlopen(ex)
  	data = json.load(obj)
  	#venue_id = data["response"]["groups"][0]["items"][0]["venue"]["id"]
  	venue_id = data["response"]["venues"][0]["categories"][0]["id"]
  	#venue_name = data["response"]["groups"][0]["items"][0]["venue"]["name"]
  	print("id : {}, name : ".format(venue_id))
#https://api.foursquare.com/v2/venues/search?ll=37.783207,-122.441673&limit=50&categoryId=4d4b7105d754a06374d81259&intent=checkin&radius=520&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20120721
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