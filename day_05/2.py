# Read the instructions from the file
with open('input') as f:
  instructions = f.readlines()

# Remove leading/trailing white space and newlines
instructions = [x.strip() for x in instructions]

# Initialize the stacks
stacks = [
        ['F', 'C', 'P', 'G', 'Q', 'R'], 
        ['W', 'T', 'C', 'P'], 
        ['B', 'H', 'P', 'M', 'C'],
        ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
        ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
        ['D', 'P', 'J'],
        ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
        ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
        ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W'],
      ]

# Follow the instructions to rearrange the crates
for instruction in instructions:
  # Parse the instruction
  words = instruction.split()
  n = int(words[1])
  from_stack = int(words[3]) - 1
  to_stack = int(words[5]) - 1

  # Move all the crates at once
  crates = stacks[from_stack][-n:]
  stacks[from_stack] = stacks[from_stack][:-n]
  stacks[to_stack].extend(crates)

# Extract the top crates of each stack
top_crates = [stack[-1] for stack in stacks]

# Combine the top crates to get the message
message = ''.join(top_crates)

print(message)  # Output: MCD

