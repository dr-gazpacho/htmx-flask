from flask_pymongo import PyMongo
from typing import TypedDict

class Product(TypedDict):
    id: int
    category: int
    name: str
    quantity_available: int
    color: list[str]
    description: str
    price: int

strange_orb=Product(
    id=1,
    category=1,
    name='Strange Orb',
    quantity_available=20,
    color=['red', 'blue'],
    description='A strange orb that seems to contain the screams of countless souls',
    price=15
)

beguiling_elixer=Product(
    id=2,
    category=1,
    name='Beguiling Elixer',
    quantity_available=20,
    color=['red', 'blue'],
    description='It tastes really bad, otherwise it\'s positively potable',
    price=195
)

mysterious_vapor=Product(
    id=3,
    category=2,
    name='Mysterious Vapor',
    quantity_available=100,
    color=['pink', 'aqua', 'blue'],
    description='A mysterious vapor that seems to contain portals into worlds beyond',
    price=23
)

questionable_evidence=Product(
    id=4,
    category=2,
    name='Questionable Evidence',
    quantity_available=32,
    color=['white', 'grey'],
    description='Certainly it could mean what we think it means, but does it? Origin, unknown.',
    price=10
)

generic_meat=Product(
    id=5,
    category=3,
    name='Generic Meat',
    quantity_available=5,
    color=['grey'],
    description='Meat from a meat producing entity',
    price=1
)

forgettable_corn=Product(
    id=6,
    category=3,
    name='Forgettable Corn',
    quantity_available=7,
    color=['yellow', 'jeweled', 'blue'],
    description='Corn, not unlike every single ear of corn you have ever seen; unremarkable',
    price=2
)

initial_values=[strange_orb, beguiling_elixer, mysterious_vapor, questionable_evidence, generic_meat, forgettable_corn]

def create_mock_data(mongo: PyMongo):
    try:
        contents=mongo.db.inventory.count_documents({})
        if not contents:
            # if the inventory is totally empty, initialize with these three dummy items
            for product in initial_values:
                mongo.db.inventory.insert_one(product)
        else:
            # get all documents in inventory, and print them to console just so you can see what you have
            collection=mongo.db.inventory.find({})
            for doc in collection:
                print(doc)
    except:
        # semantic exception message, very helpful
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
#     user=someone
#     cartItem = me.EmbeddedDocumentListField(CartItem)