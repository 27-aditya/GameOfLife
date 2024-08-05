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
            if random_number >= 0.5:
                state[i][j] = 1
            else:
                state[i][j] = 0
    return state
    
def render(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 1:
                print('#', end=' ')
            else:
                print('_', end=' ')
        print()
        
matrix = random_state(height, width)
        
render(matrix)
    

    
