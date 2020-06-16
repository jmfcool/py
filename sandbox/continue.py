array = ["alpha","bravo","charlie"]

# Break

for item in array:
    if item == "bravo":
        print("Item {0}".format(item))
        break
    print("Item {0}".format(item))

# Continue

for item in array:
    if item == "bravo":
        continue
    print("Item {0}".format(item))