# libraries
from flask import Flask, render_template
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
mongo = PyMongo(app)
# create a few items in the db if its empty
create_mock_data(mongo) 

@app.route("/")
def home():
    if htmx:
        return render_template("partials/thing.html")
    return render_template("index.html")

@app.route("/clicked", methods=["POST"])
@templated("./partials/test.html")
def clickedOut():
    return dict(name="Arthur", king_of="The_Britons")

# @app.route("/clickedOutTwo", methods=["POST"])
# def clickedOutTwo():
#     return render_template("./partials/test.html", name="Arthur", king_of="The_Britons")

# app.run(debug=True)