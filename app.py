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

@app.route("/shelf", methods=["GET", "POST"])
@templated("./partials/shelf.html")
def shelf():
    shelf=mongo.db.inventory.find({})
    if request.method == 'POST':
        method=request.form.get('method')
        shelf=mongo.db.inventory.find({}).sort(method)
    return dict(shelf=shelf)

@app.route("/add", methods=["POST"])
@templated("./partials/cart.html")
def cart():
    product=int(request.form.get("product"))
    new_addition_to_cart=mongo.db.cart.find_one({'product_id': product})
    print(new_addition_to_cart)
    if new_addition_to_cart is None:
        item_from_inventory=mongo.db.inventory.find_one({'product_id': product})
        item_from_inventory["quantity_in_cart"]=item_from_inventory.get("quantity_in_cart", 0)+1
        mongo.db.cart.insert_one(item_from_inventory)
        cart=mongo.db.cart.find({})
        return dict(cart=cart)
    else:
        item_from_cart=mongo.db.cart.find_one({'product_id': product})
        quantity=int(item_from_cart.get("quantity_in_cart"))+1

        mongo.db.cart.update_one(
            {'product_id': product},
            {"$set": {"quantity_in_cart": quantity}}
        )
        cart=mongo.db.cart.find({})
        return dict(cart=cart)

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