import numpy as np


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------

    
    init = np.array(init)
    grid = np.array(grid)
    goal = np.array(goal)
    
    
    closed = np.zeros(grid.shape)
    closed[tuple(init)] = 1
    
    expand = -np.ones(grid.shape)
    
    x,y = init
    g = 0
    open = [[g,x,y]]
    
    found = False    # found goal
    resign = False   # no expand
    
    result = ""
    count = 0
    while found is False and resign is False:
        if len(open) == 0:
            resign = True
            result = "fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            g,x,y = next 
            expand[x, y] = count
            count += 1
            
            if np.array_equal([x,y],goal):
                found = True
                result = next
            else:
                for i in range(len(delta)):
                    x2,y2 = np.array([x,y]) + delta[i]
                    if in_grid([x2, y2], grid) \
                            and closed[x2][y2] == 0 \
                            and grid[x2][y2] == 0:

                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1
    print(result)
    return expand



def in_grid(new_pos, grid):
    height,width = grid.shape
    
    return      new_pos[0] >=0 and new_pos[0] < height \
            and new_pos[1] >=0 and new_pos[1] < width



search(grid,init,goal,cost)





#################
# output:
# [[  0,   1,  -1,  11,  15,  18],
#  [  1,   3,   5,   8,  12,  16],
#  [  4,   6,  -1,  13,  -1,  19],
#  [  7,   9,  -1,  17,  -1,  21],
#  [ 10,  14,  -1,  20,  -1,  22]]
################