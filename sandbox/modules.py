import classes

alpha = classes.Foo("alpha")
print(alpha.get_capitalize())

from classes import Foo

bravo = Foo("bravo")
print(bravo.lget_capitalize())