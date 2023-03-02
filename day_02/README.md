# Day 2: Rock Paper Scissors

To solve this problem, we need to interpret the strategy guide and apply the rules of the Rock Paper Scissors game to each round of the tournament.

First, we need to create a mapping from the letters in the strategy guide to the shapes they represent in the game. We can do this by creating a dictionary with keys (A and X), (B and Y), and (C and Z), and values Rock, Paper, and Scissors, respectively.

- Next, we need to loop through each round in the strategy guide and determine the outcome of the round. 
- For each round, we can use the dictionary we created to convert the opponent's move and our move to their corresponding shapes. 
- Then, we can use the rules of the game to determine the outcome of the round and calculate the score for that round. 
- Finally, we can add the score for the shape that we selected and the round's score to the total score.
- Possible [solution](1.py).

## Part Two

- To calculate the total score based on the Elf's instructions for the second column, we need to modify the code to choose the shape that we need to play in order to achieve the desired outcome for each round.
- Possible [solution](2.py).
