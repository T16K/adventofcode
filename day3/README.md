# Day 3: Rucksack Reorganization

To solve this problem, we can loop through each rucksack and check the items in each compartment. If we find an item type that appears in both compartments, we can add its priority to a running total and continue to the next rucksack.
- Possible [solution](1.py)

## Part Two

To solve this problem, we can loop through the list of rucksacks three at a time and check the items in each rucksack. If we find an item type that appears in all three rucksacks, we can add its priority to a running total and continue to the next group of three rucksacks.
- Possible [solution](2.py)
