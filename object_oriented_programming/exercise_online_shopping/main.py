from user import User


brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.availability)  # => True
mary.buy_product(keyboard)
print(keyboard.availability)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
review in mary.reviews  # => True
review in keyboard.reviews  # => True