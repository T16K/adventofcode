# Day 5: Supply Stacks

To solve this problem, we can simulate the rearrangement procedure by following the given instructions and keeping track of the top crate of each stack.

- We can represent each stack as a list, with the bottom crate at the beginning of the list and the top crate at the end. For example, the initial state of the stacks can be represented as:
```py
stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
```
- We can then iterate through the rearrangement instructions and update the stacks accordingly. For example, the first instruction "move 1 from 2 to 1" means we need to move the top crate (D) from stack 2 to stack 1. We can implement this as follows:
```py
from_stack = 2
to_stack = 1
n = 1

for i in range(n):
  crate = stacks[from_stack].pop()
  stacks[to_stack].append(crate)
```
- We can repeat this process for each instruction in the rearrangement procedure to obtain the final state of the stacks.
- Finally, we can extract the top crate of each stack by accessing the last element of each list and combine them together to get the message that the Elves need.
- Possible [solution](1.py).

## Part Two

To solve this problem, we need to update the solution to simulate the CrateMover 9001, which can move multiple crates at once and keeps them in the same order.

- One way to do this is to change the loop that moves the crates to move all of them at once, rather than one at a time. 
- We can do this by using the extend method of a list to add the crates from the source stack to the destination stack in one go.
- Possible [solution](2.py).
