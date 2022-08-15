from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

#add the following to set up Flask:
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#set up our Flask routes: one for the main HTML page everyone will visit 
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#set up our Flask routes to scrape data
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
#gathered new data

#Flask is to tell it to run.
if __name__ == "__main__":
   app.run()