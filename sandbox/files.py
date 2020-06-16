array = []

def get_item():
    item_title = []
    for item in array:
        item_title.append(array)
    return item_title

def print_item():
    item_title = get_item()
    print(item_title)

def add_item(item, id=1):
    record = {"item": item, "id": id}
    array.append(record)
    print(id)

def save_file(item):
    try:
        f = open("array.txt", "a")
        f.write(item, "\n")
        f.close()
    except Exception:
        print("Could not save file!")

def read_file():
    try:
        f = open("array.txt", "r")
        for item in f.readlines():
            add_item(item)
        f.close()
    except Exception:
        print("Could not read file!")

read_file()
print_item()

item = input("Enter item name: ")
id = input("Enter id: ")

add_item(item, id)
save_file(item)