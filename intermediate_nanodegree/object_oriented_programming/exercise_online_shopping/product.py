class Product:
    def __init__(self, name, description, seller, price, availability):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Product({self.name}, {self.description}) at ${self.price}"
