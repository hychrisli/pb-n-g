from abc import ABC


class Product: 

    def __init__(**kwargs):
        self.id = id
        self.name = name
        self.price = price
        self.desciption = description


class Account:

    def __init__(**kwargs):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

class ShoppingCart:

    def __init__(**kwargs):
        self.cartItems = dict() # key: prouduct.id, value: quantity


    def add_product(self, product_id, quantity):
        pass

    def adjust_quantity(self, product_id, quantity):
        pass

    def remove_product(self, product_id):
        pass


class Order:
    def __init__(**kwargs):
        self.items = dict()
        self.status = OrderStatus.NEW


    def add_product(self, product_id, quantity):
        pass

    def adjust_quantity(self, product_id, quantity):
        pass

    def remove_product(self, product_id):
        pass

    def set_shipping_address(self):
        pass
    
    def update_order_status(self, status):
        self.status = status
    

class Shipping:

    def __init__(**kwargs):

        self.order = order
        self.status = ShippingStatus.NEW

    def update_shipping_status(self, status):
        self.status = status

    def track_shipping_details(self):
        pass


class Address:

    def __init__(self, **kwargs):

        self.address = address
        self.city = city
        self.state = state


class Review:

    def __init__(self, **kwargs):
        
        def.id = id
        def.product_id = product_id
        def.account_id = account_id
        def.stars = stars
        def.comments = comments

    def edit_review(self, stars, comments):
        pass
    
