from flask_pymongo import PyMongo
from typing import TypedDict

class Item(TypedDict):
    id: int
    category: int
    name: str
    quantity_available: int
    color: list[str]
    description: str
    price: int


strange_orb=Item(
    id=1,
    category=1,
    name='Strange Orb',
    quantity_available=20,
    color=['red', 'blue'],
    description='A strange orb that seems to contain the screams of countless souls',
    price=15
)

mysterious_vapor=Item(
    id=2,
    category=2,
    name='Mysterious Vapor',
    quantity_available=100,
    color=['pink', 'aqua', 'blue'],
    description='A mysterious vapor that seems to contain portals into worlds beyond',
    price=10
)

forgettable_corn=Item(
    id=3,
    category=3,
    name='Forgettable Corn',
    quantity_available=7,
    color=['yellow', 'jeweled', 'blue'],
    description='Corn, not unlike every single ear of corn you have ever seen; unremarkable',
    price=2
)

initial_values=[strange_orb, mysterious_vapor, forgettable_corn]

def create_mock_data(mongo: PyMongo):
    try:
    # get all stuff from db
        contents=mongo.db.inventory.count_documents({})
        if not contents:
            for item in initial_values:
                mongo.db.inventory.insert_one(item)
        else:
            collection=mongo.db.inventory.find({})
            for doc in collection:
                print(doc)
    except:
        raise Exception('Some way, somehow, something is all jacked up with the connection to your database')
        
# Here temporarily until I figure out how to initialize this database

# use them on the shelf and update on restock
# class Item(Document):
#     name = StringField(required=True)
#     id = IntField()
#     quantityRemaining = IntField()
#     colors = ListField()
#     description = StringField()
#     price = IntField()

# # when things enter the cart they get expanded with how many of them there are in the cart and who it belongs to
# class CartItem(me.EmbeddedDocument):
#     shopper = me.StringField()
#     item = me.EmbeddedDocumentField(Item)
#     quantityInCary = me.IntField()

# # maybe persist the idea of the cart as its own document in db
# class Cart(me.Document):
#     cartItem = me.EmbeddedDocumentListField(CartItem)