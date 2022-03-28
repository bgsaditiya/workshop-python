class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

 d = Dog('Fido')
 e = Dog('Buddy')
 d.kind                  # shared by all dogs
#'canine'
 e.kind                  # shared by all dogs
#'canine'
 d.name                  # unique to d
#'Fido'
 e.name                  # unique to e
#'Buddy'



class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

 d = Dog('Fido')
 e = Dog('Buddy')
 d.add_trick('roll over')
 e.add_trick('play dead')
 d.tricks                # unexpectedly shared by all dogs
#['roll over', 'play dead']



class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

 d = Dog('Fido')
 e = Dog('Buddy')
 d.add_trick('roll over')
 e.add_trick('play dead')
 d.tricks
#['roll over']
 e.tricks
#['play dead']