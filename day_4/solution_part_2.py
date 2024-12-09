def count_xmas_patterns(grid):
    def is_valid_xmas(x, y):
        # Check top-left to bottom-right diagonal (MAS or SAM)
        if (
            x >= 1 and y >= 1 and x < len(grid) - 1 and y < len(grid[0]) - 1 and
            ((grid[x-1][y-1] == 'M' and grid[x][y] == 'A' and grid[x+1][y+1] == 'S') or
             (grid[x-1][y-1] == 'S' and grid[x][y] == 'A' and grid[x+1][y+1] == 'M'))
        ):
            # Check top-right to bottom-left diagonal (MAS or SAM)
            if (
                ((grid[x-1][y+1] == 'M' and grid[x][y] == 'A' and grid[x+1][y-1] == 'S') or
                 (grid[x-1][y+1] == 'S' and grid[x][y] == 'A' and grid[x+1][y-1] == 'M'))
            ):
                return True
        return False

    # Convert the input grid into a 2D list of characters
    count = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 'A' and is_valid_xmas(i, j):
                count += 1

    return count


with open("day_4/input.txt", 'r') as f:
    wordsearch = [line.strip() for line in f.readlines()]

# Calculate the result
result = count_xmas_patterns(wordsearch)
print("Count of X-MAS patterns:", result)
