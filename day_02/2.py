# Create a dictionary to map the letters in the strategy guide to the corresponding shapes
SHAPE_MAP = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    }

# Initialize the total score to 0
total_score = 0

# Read the strategy guide from the input file
with open("input") as input_file:
    strategy_guide = input_file.readlines()

# Loop through each round in the strategy guide
for round in strategy_guide:

    # Split the round string into two parts: the opponent's move and our move
    opponent_move, outcome = round.split()

    # Use the dictionary to convert the letters to their corresponding shapes
    opponent_move = SHAPE_MAP[opponent_move]

    # Determine the shape that we need to play in order to achieve the desired outcome
    if outcome == "X":
        # We need to lose, so choose the shape that defeats the opponent's move
        if opponent_move == "Rock":
            our_move = "Scissors"
        elif opponent_move == "Paper":
            our_move = "Rock"
        else:
            our_move = "Paper"
    elif outcome == "Y":
        # We need to end in a draw, so choose the same shape as the opponent
            our_move = opponent_move
    else:
        # We need to win, so choose the shape that is defeated by the opponent's move
        if opponent_move == "Rock":
            our_move = "Paper"
        elif opponent_move == "Paper":
            our_move = "Scissors"
        else:
            our_move = "Rock"

    # Determine the outcome of the round
    if opponent_move == our_move:
        # The round is a draw, add 3 to the total score
        total_score += 3
    elif (opponent_move == "Rock" and our_move == "Paper") or (opponent_move == "Paper" and our_move == "Scissors") or (opponent_move == "Scissors" and our_move == "Rock"):
        # We won the round, add 6 to the total score
        total_score += 6
    else:
        # We lost the round, add 0 to the total score
        total_score += 0

    # Calculate the score for this round by adding the score for the shape we chose
    # to the score for the outcome of the round
    if our_move == "Rock":
        round_score = 1 
    elif our_move == "Paper":
        round_score = 2
    else:
        round_score = 3

    # Add the round score to the total score
    total_score += round_score

# Print the final total score
print(total_score)
