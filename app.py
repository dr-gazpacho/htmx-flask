# libraries
from flask import Flask, render_template, request
from flask_htmx import HTMX, make_response
from flask_pymongo import PyMongo
# this project
from utils.template_decorator import templated
from utils.products import create_mock_data

# initialize flask, htmx
app=Flask(__name__)
htmx=HTMX(app)
# set up database connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/htmx_flask"
mongo=PyMongo(app)
# create a few items in the db if its empty
create_mock_data(mongo) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shelf", methods=["POST"])
@templated("./partials/shelf.html")
def getShelf():
    shelf_one=mongo.db.inventory.find({}).sort("category")
    shelf_two=mongo.db.inventory.find({}).sort("category")
    shelf_three=mongo.db.inventory.find({}).sort("category")
    # I hate doing this shelf one/two thing

    return dict(shelf_one=shelf_one, shelf_two=shelf_two, shelf_three=shelf_three)

@app.route("/thing", methods=["POST"])
@templated("./partials/thing.html")
def makeNewThing():
    name=request.form.get("thing-name")
    description=request.form.get("thing-description")
    return dict(name=name, description=description)

# still need to work on this
    # I need to return SOMETHING to the FE, maybe just remove the clicked element from the DOM and add it to the 'cart'
    # I think I need to make the color an input, have the button deactivated? then able to submit on color click?
# @app.route("/addToCart", methods=["POST"])
# def addToCart():
#     color=request.args.get('color')
#     item=request.args.get('henry')
#     print(color, item)
#     return '1'

# app.run(debug=True)