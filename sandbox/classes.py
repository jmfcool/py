array = []

class Foo:

    name = "charlie"

    def __init__(self, item, id=1):
        self.item = item
        self.id = id
        array.append(self)

    def __str__(self):
        return "Item: " + self.item

    def get_capitalize(self):
        return self.item.capitalize()

    def get_name(self):
        return self.name

alpha = Foo("alpha")
print(alpha.get_capitalize())

bravo = Foo("bravo")
print(bravo.get_capitalize())

print(array)
print(Foo.name)

class Bar(Foo):

    name = "delta"

    def get_capitalize(self):
        foo = self.item.capitalize()
        return foo + "-bar"

    def get_name(self):
        return "This is overriding the Method of the parent class!"

echo = Bar("echo")

print(echo.get_capitalize())
print(echo.get_name())

print(array)
print(Bar.name)