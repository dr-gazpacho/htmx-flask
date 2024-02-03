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