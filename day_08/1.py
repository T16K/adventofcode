# read the input
tree_map = []
with open('input') as f:
    for line in f:
        tree_map.append(list(map(int, line.strip())))

n_rows = len(tree_map)
n_cols = len(tree_map[0])

# count visible trees
visible_count = 0
for row in range(n_rows):
    for col in range(n_cols):
        tree_height = tree_map[row][col]
        visible_from_left = all(tree_height > tree_map[row][c] for c in range(col))
        visible_from_right = all(tree_height > tree_map[row][c] for c in range(col+1, n_cols))
        visible_from_top = all(tree_height > tree_map[r][col] for r in range(row))
        visible_from_bottom = all(tree_height > tree_map[r][col] for r in range(row+1, n_rows))
        if any((visible_from_left, visible_from_right, visible_from_top, visible_from_bottom)):
            visible_count += 1

print(visible_count)
