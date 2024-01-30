from flask import Flask, render_template
from flask_htmx import HTMX

app=Flask(__name__)
htmx = HTMX(app)

@app.route("/")
def home(): 
    if htmx:
        return render_template("partials/thing.html")
    return render_template("index.html")

@app.route("/clicked", methods=["POST"])
def clicked():
    print('clicked')
    return 'string'