array = {
        "item": "alpha",
        "id": 1234,
        "notes": None
    }

print(array["id"])

# Print keys

print(array.keys())

# Print values

print(array.values())

# Change value of item

array["item"] = "bravo"
print(array.values())

# Delete item

del array["item"]
print(array.values())