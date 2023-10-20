# Define the numbers in a list
numbers = [1, -1, 8, -5]

# Initialize the minimum value to the first number in the list
min_value = numbers[0]

# Iterate through the list to find the minimum value
for num in numbers:
    if num < min_value:
        min_value = num

# 'min_value' now contains the minimum value among the numbers
print("The minimum value is:", min_value)