# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create the instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsmission")

# Route to render index.html template using data from Mongo
@app.route('/')
#
def index():
    mars_report = mongo.db.mars_report.find_one()
    print(mars_report)
    return render_template('index.html', mars=mars_report)


@app.route('/scrape')
def scrape():
    mars_report = mongo.db.mars_report
    mars = scrape_mars.scrape()
    mars_report.update(
        {},
        {"$set": mars},
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)