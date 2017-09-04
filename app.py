from urllib.request import urlopen
import json
from flask import Flask
from flask import render_template
from flask import request
from location_lat_lng import location
from fs_images import get_images


app = Flask(__name__)
GL = location()
GI = get_images()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=['POST'])
def search_location():
    location_name = request.form.get('destination')
    lat, lng = GL.get_lat_lng(location_name)
    arr = GI.get_img(lat, lng)
    return render_template("result.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
