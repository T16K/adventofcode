def count_fully_contained_pairs(pairs):
  count = 0
  for pair in pairs:
    range1, range2 = pair.split(',')
    start1, end1 = map(int, range1.split('-'))
    start2, end2 = map(int, range2.split('-'))
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
      count += 1
  return count

# Open the file and read the lines
with open('input', 'r') as f:
  pairs = f.readlines()

# Strip the newline characters from the end of each line
pairs = [line.strip() for line in pairs]

print(count_fully_contained_pairs(pairs))
