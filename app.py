from flask import Flask, render_template
from flask_htmx import HTMX

app=Flask(__name__)
htmx = HTMX(app)

@app.route("/")

def hello(): 
    message = "Hello, World!"
    return render_template('index.html',  
                           message=message) 