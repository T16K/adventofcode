def find_badges(rucksacks):
    # Set up a running total for the sum of the priorities of the badge item types
    total_priority = 0
    
    # Loop through the rucksacks three at a time
    for i in range(0, len(rucksacks), 3):
        # Get the rucksacks for this group of three
        group1 = rucksacks[i]
        group2 = rucksacks[i + 1]
        group3 = rucksacks[i + 2]
        
        # Loop through each item type in the first rucksack
        for item in group1:
            # Check if the item type also appears in the second and third rucksacks
            if item in group2 and item in group3:
                # If it does, add its priority to the running total
                total_priority += get_priority(item)
                break
    
    return total_priority

def get_priority(item):
    # Convert the item to its ASCII value
    ascii_value = ord(item)
    
    # If it is a lowercase letter, its priority is its ASCII value - 96
    if ascii_value >= 97 and ascii_value <= 122:
        return ascii_value - 96
    # If it is an uppercase letter, its priority is its ASCII value - 38
    elif ascii_value >= 65 and ascii_value <= 90:
        return ascii_value - 38

# Read the rucksacks from the input file
with open('input', 'r') as f:
    rucksacks = f.readlines()

# Strip the newline characters from the end of each line
rucksacks = [x.strip() for x in rucksacks]

# Print the sum of the priorities of the badge item types
print(find_badges(rucksacks))
