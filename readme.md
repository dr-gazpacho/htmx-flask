## I know nothing about the web
Therefore, I'm trying to get better. Standing up a little toy app with HTMX/Flask because I don't know either of them

## Prerecs
- Python3
- Pip
- MongoDB
-- https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/


## Eat Your Vegetables
- https://htmx.org/docs/
- https://flask.palletsprojects.com/en/2.3.x/quickstart/
- https://flask.palletsprojects.com/en/2.3.x/patterns/mongoengine/

## General Notes
- Using this templating decorator to separate the html out of the main `app` and hopefully makes it a little more readable
-- https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/#templating-decorator
- Flask uses Jinja (Jinja2?) as a templating engine, that allows Python to access the HTML/HTMX via jazz like `{{ some_python }}`

## Get That Python Up & Runnin'
From the root of the project, spin up a virtual enviroment, activate it, and install some goodies
1. `python3 -m venv .venv`
1. `. .venv/bin/activate`
1. `pip install Flask-PyMongo`

## Get That DB Up & runnin
Get MongoDB installed on your machine, then you'll open a connection to it before you run the app. 
The app will be set up to initialize with some shoddy mock data 
- https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
1. `brew services start mongodb-community@7.0`
1. `brew services list` will show you running services
1. `mongosh` will initialize a connection from the command line
 - while running mongosh, you can use `show dbs` to see a list of all databases
    - if you need to drop your dbs/collections because you're like me and kinda dumb
    - `use dbName` for this I have it set as `use htmx_flask`
    - then drop a specific collection `db.COLLECTION_NAME.drop()`
    - or drop the whole mess `db.dropDatabase()`
1. `brew services stop mongodb-community@7.0` will stop your MongoDB when you're done

Going to keep this to a real minimum of deps. Once you got all that python and mongo installed, you can run the app this like:
1. `brew services start mongodb-community@7.0`
1. `flask run` - the first time you start it, the app will create some initial data for your local db. Or it will throw an exception if you totally screwed up.
1. On your browswer go to `http://127.0.0.1:5000`
1. Rejoice


It'll serve the HTML with the local copy of HTMX. And some mock data Live it. Breathe It. Rejoice.

Power down the server and tear down your virtual environment when you're done
1. `deactivate`

Rejoice

## But wait there's more
Some to-do things I'd like to try to flesh this out
- Active search so you can see what other weird shit exists 
-- https://htmx.org/examples/active-search/