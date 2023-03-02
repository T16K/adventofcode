# Read the input from a file
with open('input', 'r') as f:
    input_lines = f.readlines()

# Remove leading/trailing whitespace from each line
input_lines = [line.strip() for line in input_lines]

# Create an empty list to store the total number of Calories for each Elf
calories = []

# Create a variable to store the total number of Calories for the current Elf
current_elf_calories = 0

# Process each line in the input
for line in input_lines:
    # If the line is empty, it indicates that we have reached the end of the
    # inventory for the current Elf
    if line == '':
        # Add the total number of Calories for the current Elf to the list
        calories.append(current_elf_calories)
        # Reset the total number of Calories for the current Elf to 0
        current_elf_calories = 0
    else:
        # Otherwise, the line contains the number of Calories for a single food
        # item. We add this number to the total number of Calories for the
        # current Elf.
        current_elf_calories += int(line)

# Add the final total number of Calories for the current Elf to the list
calories.append(current_elf_calories)

# Sort the list of Calories in descending order
calories.sort(reverse=True)

# Find the sum of the top three Elves carrying the most Calories
top_three_calories = sum(calories[:3])

# Print the result
print(top_three_calories)
