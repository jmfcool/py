array = ["alpha","bravo","charlie"]

# Access left to right

print(array[1])
print(array)

# Access right to left

print(array[-2])
print(array)

# Replace item in Array

print(array[2])
print(array)

array[2] = "delta"

print(array[2])
print(array)

# Append new item to Array

array.append("echo")

print(array[3])
print(array)

# Check for item in Array

print("charlie" in array == True)

print("echo" in array == True)

# Check length of Array

print(len(array))

# Delete item from Array

del array[1]
print(array)

# Slice Array

print(array[2:])

print(array[0:-1])