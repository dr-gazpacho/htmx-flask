from flask import Flask, render_template
from flask_htmx import HTMX, make_response
from flask_pymongo import PyMongo
# initialize flask, htmx
app=Flask(__name__)
htmx = HTMX(app)
# set up db connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def home(): 
    if htmx:
        return render_template("partials/thing.html")
    return render_template("index.html")

@app.route("/clicked", methods=["POST"])
def clicked():
    return '<div hx-swap="innerHTML" id="switch" hx-trigger="click" hx-post="/clickedOff" hx-target="#switch">the switchback</div>'

@app.route("/clickedOff", methods=["POST"])
def clickedOff():
    return '<div id="beforeend" hx-swap="innerHTML" hx-trigger="click" hx-post="/clicked" hx-target="#switch">the switch</div>'

@app.route("/clickedOut", methods=["POST"])
def clickedOut():
    return make_response(
        'ope',
        push_url=False,
        trigger={"event1": "A message", "event2": "Another message"},
    )