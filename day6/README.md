# Day 6: Tuning Trouble

To solve this problem, you can iterate through the characters in the datastream buffer one at a time, and keep track of the four most recent characters in a list. For each character, you can check whether the list contains any duplicates, and if it doesn't, you can return the index of that character in the buffer.
- Possible [solution](1.py).

## Part Two

To solve this problem, you can modify the function that you wrote earlier to look for a sequence of 14 distinct characters instead of 4. You can do this by changing the length of the `recent_chars` list and the value that is compared to the length of the set of the `recent_chars` list.
- Possible [solution](2.py).
