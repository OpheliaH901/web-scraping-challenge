
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
# import necessary libraries
from flask import Flask, render_template
import pymongo
# import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)