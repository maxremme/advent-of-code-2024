

def count_occurrences(matrix, word):
    rows = len(matrix)             
    cols = len(matrix[0])          
    word_length = len(word)        
    count = 0                      

    # Helper function to check if a cell is within bounds
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Recursive function to search for the word in one direction
    def search(r, c, index, dr, dc):
        if index == word_length:   # Base case: full word found
            return 1
        if not is_valid(r, c) or matrix[r][c] != word[index]: # Out of bounds or mismatch
            return 0
        # Move to the next cell in the current direction
        return search(r + dr, c + dc, index + 1, dr, dc)

    # 8 possible directions
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]

    # iterate over each cell
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == word[0]:  # start of the word
                for dr, dc in directions: # Check directions
                    count += search(r, c, 0, dr, dc)

    return count



with open("day_4/input.txt", 'r') as f:
    wordsearch = [line.strip() for line in f.readlines()]

word = "XMAS"
result = count_occurrences(wordsearch, word)
print("Occurrences of 'XMAS':", result)




