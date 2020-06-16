array = ["alpha"]

def get_item():
    item_title = []
    for item in array:
        item_title = array
    return item_title

def print_item():
    item_title = get_item()
    print(item_title)

def add_item(item, id=1):
    record = {"item": item, "id": id}
    array.append(record)
    print(id)

print_item()

add_item(item="bravo", id=42)

print_item()

# Arguments

def args(item, *args):
    print(item)
    print(args)

args("Charlie", "delta", "echo", "foxtrot")

def args(item, **kwargs):
    print(item)
    print(kwargs["foo"], kwargs["bar"])

args("Charlie", foo="delta", bar="echo")

# Nested

def get_items():

    array = ["alpha", "bravo"]

    def get_item():
        item_title = []
        for item in array:
            item_title.append(item.title())
        return item_title

        print_title = get_item()
        print(print_title)

# Yield

def read_file():
    try:
        f = open("array.txt", "r")
        for item in read_items(f):
            add_item(item)
        f.close()
    except Exception:
        print("Could not read file!")

def read_items(f):
    for line in f:
        yield line

read_file()
print(array)

# Lambda

double = lambda x: x * 2
print(double(150))