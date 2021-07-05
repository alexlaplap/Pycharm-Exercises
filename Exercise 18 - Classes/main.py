class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello {self.name}.")


a = input('Name: ')
name = Person(a)
name.talk()

b = input('Name: ')
name = Person(b)
name.talk()