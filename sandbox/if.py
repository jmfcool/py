alpha = 10

# if else statment

if alpha == 10:
    print("Alpha is 10")
else:
    print("Alpha not 10")

# Truthy

if alpha:
    print("Number is defined and is truthy")

bravo = "bravo"

if bravo:
    print("Text is defined and is truthy")

# Executes

charlie = True

if charlie:
    print("This will execute")

# Will not execute

delta = None

if delta:
    print("This will not execute")

if alpha != 10:
    print("This will not execute")

if not charlie:
    print("This will not execute")

# Multiple arguments

if alpha == 10 and charlie:
    print("This will execute")

if alpha == 20 or charlie:
    print("This will execute")

# Ternary

echo = 9

print("foo" if alpha > echo else "bar")