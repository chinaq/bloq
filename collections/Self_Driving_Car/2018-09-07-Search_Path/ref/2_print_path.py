import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    action = - np.ones(np.array(grid).shape, dtype=int)

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                            
    # policy = np.chararray(action.shape)
    policy = np.ndarray(action.shape, dtype='S1')
    policy[:] = ' '
    x,y = goal
    policy[x][y] = '*'
    
    while not np.array_equal([x,y], init):
        x2,y2 = np.array([x,y]) - delta[action[x][y]]
        policy[x2][y2] = delta_name[action[x][y]]
        x,y = x2,y2

    return policy # make sure you return the shortest path
    
    

print(search(grid,init,goal,cost))





########################
# output:
# [['>' 'v' ' ' ' ' ' ' ' ']
#  [' ' '>' '>' '>' '>' 'v']
#  [' ' ' ' ' ' ' ' ' ' 'v']
#  [' ' ' ' ' ' ' ' ' ' 'v']
#  [' ' ' ' ' ' ' ' ' ' '*']]
########################