# This script prints a pyramid pattern of stars.
tree = 5

for i in range(1, tree + 1): # Loop through each level of the pyramid
    print(" " * (tree - i) + "*" * (2 * i - 1)) # Print spaces and stars for the current level
# The number of spaces decreases while the number of stars increases as we go down the levels.