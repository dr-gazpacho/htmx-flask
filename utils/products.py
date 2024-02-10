from flask_pymongo import PyMongo
from typing import TypedDict

class Product(TypedDict):
    product_id: int
    category: int
    category_class: str
    name: str
    color: list[str]
    description: str
    price: int
    card_id: int
    quantity_in_cart: int

strange_orb=Product(
    product_id=1,
    category=1,
    category_class='trapped-entity',
    name='Strange Orb',
    color=['midnightblue', 'royalblue'],
    description='A strange orb that seems to contain the screams of countless souls',
    price=15,
    cart_id=0,
    quantity_in_cart=0
)

beguiling_elixer=Product(
    product_id=2,
    category=1,
    category_class='trapped-entity',
    name='Beguiling Elixer',
    color=['midnightblue', 'royalblue'],
    description='It tastes really bad, otherwise it\'s positively potable',
    price=195,
    cart_id=0,
    quantity_in_cart=0
)

mysterious_vapor=Product(
    product_id=3,
    category=2,
    category_class='transient-horror',
    name='Mysterious Vapor',
    color=['red', 'coral', 'midnightblue'],
    description='A mysterious vapor that seems to contain portals into worlds beyond',
    price=23,
    cart_id=0,
    quantity_in_cart=0
)

questionable_evidence=Product(
    product_id=4,
    category=2,
    category_class='transient-horror',
    name='Questionable Evidence',
    color=['darkorchid', 'springgreen'],
    description='Certainly it could mean what we think it means, but does it? Origin, unknown',
    price=10,
    cart_id=0,
    quantity_in_cart=0
)

generic_meat=Product(
    product_id=5,
    category=3,
    category_class='food',
    name='Generic Meat',
    color=['springgreen'],
    description='Meat from a meat producing entity',
    price=1,
    cart_id=0,
    quantity_in_cart=0
)

forgettable_corn=Product(
    product_id=6,
    category=3,
    category_class='food',
    name='Forgettable Corn',
    color=['gold', 'darkorchid', 'midnightblue'],
    description='Corn, not unlike every single ear of corn you have ever seen; unremarkable',
    price=2,
    cart_id=0,
    quantity_in_cart=0
)

shrinking_gloves=Product(
    product_id=7,
    category=1,
    category_class='trapped-entity',
    name='Shrinking Gloves',
    color=['coral', 'midnightblue', 'springgreen'],
    description='They\'re gonna scrunch right down and squish your little fingies',
    price=144,
    cart_id=0,
    quantity_in_cart=0
)

heroic_broom=Product(
    product_id=8,
    category=1,
    category_class='trapped-entity',
    name='Heroic Broom',
    color=['springgreen', 'royalblue'],
    description='Dust trembles in fear.',
    price=2275,
    cart_id=0,
    quantity_in_cart=0
)

opaque_opening=Product(
    product_id=9,
    category=2,
    category_class='transient-horror',
    name='Opaque Opening',
    color=['springgreen'],
    description='What lies beyond? You see nothing but smell everything',
    price=765,
    cart_id=0,
    quantity_in_cart=0
)

underlying_principle=Product(
    product_id=10,
    category=2,
    category_class='transient-horror',
    name='Underlying Principle',
    color=['coral'],
    description='The unquestionable heart-o-it-all',
    price=3599,
    cart_id=0,
    quantity_in_cart=0
)

simply_fur=Product(
    product_id=11,
    category=3,
    category_class='food',
    name='Simply Fur',
    color=['red', 'gold'],
    description='Freshly juiced fur, some pulp',
    price=13,
    cart_id=0,
    quantity_in_cart=0
)

flamin_hot=Product(
    product_id=12,
    category=3,
    category_class='food',
    name='Flamin\' Hot',
    color=['red', 'coral', 'gold', 'darkorchid', 'midnightblue', 'springgreen', 'royalblue'],
    description='Multi-purpose Flamin\' Hot with standard issue applicator tabs and swabs',
    price=849,
    cart_id=0,
    quantity_in_cart=0
)

initial_values=[
    strange_orb,
    beguiling_elixer,
    mysterious_vapor,
    questionable_evidence,
    generic_meat,
    forgettable_corn,
    shrinking_gloves,
    heroic_broom,
    opaque_opening,
    underlying_principle,
    simply_fur,
    flamin_hot
]

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