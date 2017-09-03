import urllib2
import json
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def home():
    obj = urllib2.urlopen(query_i)
    data = json.load(obj)
    arr = data["response"]["photos"]["items"]
    arrer = []
    for i in arr:
        arrer.append(i["prefix"]+"height300"+i["suffix"])
    return render_template("home.html", arrer=arrer)

@app.route("/search", methods=['POST'])
def search_location():
    location_name = request.form.get('destination')
    return render_template("result.html", )

if __name__ == "__main__":
    app.run(port=5000, debug=True)
