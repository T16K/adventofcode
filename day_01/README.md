# Day 1: Calorie Counting

To solve this problem, we will need to keep track of the total number of Calories each Elf is carrying, and update a variable to store the maximum number of Calories seen so far. We can do this as follows:

- Create an empty list calories to store the total number of Calories for each Elf.
- Create a variable `max_calories` to store the maximum number of Calories seen so far, initialized to 0.
- For each line in the input:
    - If the line is empty, it indicates that we have reached the end of the inventory for the current Elf. In this case, we add the total number of Calories for the current Elf to the calories list and reset the total number of Calories for the current Elf to 0.
    - Otherwise, the line contains the number of Calories for a single food item. We add this number to the total number of Calories for the current Elf.
- After all lines have been processed, we add the final total number of Calories for the current Elf to the calories list.
- We find the maximum number of Calories in the calories list, and print this value as our output.
- Possible [solution](1.py).

## Part Two

To solve this problem, we can modify the solution above to keep track of the top three Elves carrying the most Calories, instead of just the Elf carrying the most Calories. We can do this as follows:

- Create an empty list calories to store the total number of Calories for each Elf.
- Create a list `top_calories` to store the total number of Calories for the top three Elves carrying the most Calories, initialized to the empty list.
- For each line in the input:
    - If the line is empty, it indicates that we have reached the end of the inventory for the current Elf. In this case, we add the total number of Calories for the current Elf to the calories list and reset the total number of Calories for the current Elf to 0.
    - Otherwise, the line contains the number of Calories for a single food item. We add this number to the total number of Calories for the current Elf.
- After all lines have been processed, we add the final total number of Calories for the current Elf to the calories list.
- We sort the calories list in descending order.
- We take the first three elements from the sorted calories list and add them to the `top_calories` list.
- We find the sum of the elements in the `top_calories` list, and print this value as our output.
- Possible [solution](2.py).
