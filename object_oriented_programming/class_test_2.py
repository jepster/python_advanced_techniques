class Dog:
    def __init__(self, name, **tricks):
        self.name = name
        if (bool(tricks) != False):
            self.tricks = tricks.get('tricks')
        else:
            self.tricks = set()

    def teach(self, trick):
        self.tricks.add(trick)


# Change the broken code above so that the following lines work:
#
buddy = Dog('Buddy')
pascal = Dog('Pascal')
kimber = Dog('Kimber', tricks={'lie down', 'shake'})
buddy.teach('roll over')
buddy.teach('sit')
pascal.teach('fetch')
kimber.teach('fetch')
print(buddy.tricks)  # {'sit', 'roll over'}
print(pascal.tricks)  # {'fetch'}
print(kimber.tricks)  # {'lie down', 'shake', 'fetch'}