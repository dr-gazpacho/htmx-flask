# libraries
from flask import Flask, render_template, request
from flask_htmx import HTMX, make_response
from flask_pymongo import PyMongo
# this project
from utils.template_decorator import templated
from utils.products import manage_db, manufacture_product

# initialize flask, htmx
app=Flask(__name__)
htmx=HTMX(app)
# set up database connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/htmx_flask"
mongo=PyMongo(app)
# create a few items in the db if its empty and clear the cart
manage_db(mongo) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getShelf", methods=["GET", "POST"])
@templated("./partials/shelf.html")
def shelf():
    shelf=mongo.db.inventory.find({})
    if request.method == 'POST':
        method=request.form.get('method')
        shelf=mongo.db.inventory.find({}).sort(method)
    return dict(shelf=shelf)

@app.route("/addToCart", methods=["POST"])
@templated("./partials/cart.html")
def add():
    product=int(request.form.get("product"))
    new_addition_to_cart=mongo.db.cart.find_one({'product_id': product})
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

@app.route("/removeFromCart", methods=["DELETE"])
@templated("./partials/cart.html")
def remove():
    product=int(request.form.get("product"))
    mongo.db.cart.delete_one(
            {'product_id': product}
        )
    cart=mongo.db.cart.find({})
    return dict(cart=cart)

@app.route("/addToShelf", methods=["POST"])
@templated("./partials/shelf.html")
def makeNewThing():
    name=request.form.get("name")
    description=request.form.get("description")
    price=request.form.get("price")
    manufacture_product(name, description, price, mongo)
    shelf=mongo.db.inventory.find({})
    return dict(shelf=shelf)

# app.run(debug=True)