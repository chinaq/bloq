import numpy as np

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost,delta):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    grid = np.array(grid)
    delta = np.array(delta)
    goal = np.array(goal)
    
    value = 99 * np.ones(grid.shape)
    height,width = grid.shape
    
    change = True
    while change:
        change = False
        
        for x in range(height):
            for y in range(width):
                if np.array_equal([x,y], goal):
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2,y2 = [x,y] + delta[a]
                        if x2 >=0 and x2 < height \
                                and y2 >= 0 and y2 < width:
                            v = value[x2][y2] + cost
                            if v < value[x][y]:
                                change = True
                                value[x][y] = v
                                
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
    
    
print(compute_value(grid,goal,cost,delta))





####################
# output:
# [[11. 99.  7.  6.  5.  4.]
#  [10. 99.  6.  5.  4.  3.]
#  [ 9. 99.  5.  4.  3.  2.]
#  [ 8. 99.  4.  3.  2.  1.]
#  [ 7.  6.  5.  4. 99.  0.]]
####################