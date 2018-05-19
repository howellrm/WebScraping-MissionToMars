from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars
import os

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_database
collection = db.mars_data

@app.route("/scrape")
def scrape():
    mars_dict = scrape_mars.scrape()

    print(mars_dict)
    
    collection.update(
        {},
        mars_dict,
        upsert = True
    )
    print("Data scrape complete")
    return redirect("http://localhost:5000/", code=302)

@app.route("/")
def index():
    mars_output = collection.find_one()
    return render_template("index.html", mars_output=mars_output)

if __name__ == "__main__":
    app.run(debug=True)