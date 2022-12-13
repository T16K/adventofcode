def most_calories(filename: str) -> int:
    calories = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                calories.append(int(line))
            else:
                yield sum(calories)
                calories = []
    yield sum(calories)

print(max(most_calories('input')))
