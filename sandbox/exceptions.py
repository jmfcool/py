array = {
        "item": "alpha",
        "id": 1234,
        "notes": None
    }

array["bravo"] = "charlie"

try:
    print(array["bravo"])
    try:
        array["item"] = item + 10
    except NameError as error:
        print("Error with Name")
        print(error)
except KeyError:
    print("Error finding bravo")
except Exception:
    print("Boom")