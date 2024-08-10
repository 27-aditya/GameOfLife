import random

height = int(input("Enter the height: "))
width = int(input("Enter the width: "))

def dead_state(height, width):
    board = [[0 for x in range(width)] for y in range(height)]    
    return board

def random_state(height, width):
    state = dead_state(height, width)
    for i in range(height):
        for j in range(width):
            random_number = random.random()
            state[i][j] = 1 if random_number >= 0.5 else 0
    return state
    
def render(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print('#' if state[i][j] == 1 else '_', end=' ')
        print()

matrix = random_state(height, width)
render(matrix)

def next_state(matrix):
    height = len(matrix)
    width = len(matrix[0])
    state = dead_state(height, width)
    
    # Direction vectors for the eight neighbors
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    for i in range(height):
        for j in range(width):
            neighbours = 0
            for dir in directions:
                newx = i + dir[0]
                newy = j + dir[1]
                if 0 <= newx < height and 0 <= newy < width:
                    neighbours += matrix[newx][newy]
            
            # Apply Conway's Game of Life rules
            if matrix[i][j] == 1:
                if neighbours < 2 or neighbours > 3:
                    state[i][j] = 0  # Cell dies
                else:
                    state[i][j] = 1  # Cell survives
            else:
                if neighbours == 3:
                    state[i][j] = 1  # Cell becomes alive

    render(state)
print("<------>")
next_state(matrix)
