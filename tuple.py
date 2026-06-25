
# Create an empty list
numbers = []

# Add numbers 1 to 10 using append()
for i in range(1, 11):
    numbers.append(i)

print("After append:", numbers)

# Insert 0 at the beginning
numbers.insert(0, 0)
print("After insert:", numbers)

# Sort the list
numbers.sort()
print("After sort:", numbers)

# Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# Remove the last element and store it in last_number
last_number = numbers.pop()
print("Popped number:", last_number)
print("List after pop:", numbers)

# Find the position of number 5
position = numbers.index(5)
print("Position of 5:", position)

# Clear the list
numbers.clear()

# Verify list is empty
print("Length after clear:", len(numbers))