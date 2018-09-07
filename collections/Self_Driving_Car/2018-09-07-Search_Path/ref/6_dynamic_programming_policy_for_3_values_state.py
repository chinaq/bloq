import numpy as np

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy(grid,init,goal,cost):
    grid = np.array(grid)
    
    value = 999 * np.ones((4, grid.shape[0], grid.shape[1]))
    policy = np.ndarray(value.shape, dtype='S1')
    policy[:] = ' '
    change = True

    while change:
        change = False

        for orientation in range(4):
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True
    
                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            o2 = (orientation + action[a]) % 4    # turn forward
                            x2 = x + forward[o2][0]               # go ahead 
                            y2 = y + forward[o2][1]
    
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v = value[o2][x2][y2] + cost[a]
                                if v < value[orientation][x][y]:
                                    value[orientation][x][y] = v
                                    policy[orientation][x][y] = action_name[a]
                                    change = True

    return policy

policy3D = optimum_policy(grid,init,goal,cost)    # each (orientaion, x, y) got a policy



# from policy to get solution
x,y,orientation = init
policy2D = np.ndarray(np.array(grid).shape, dtype='S1')
policy2D[:] = ' '

policy2D[x][y] = policy3D[orientation][x][y]
while policy3D[orientation][x][y] != '*':
    if policy3D[orientation][x][y] == '#':
        o2 = orientation
    elif policy3D[orientation][x][y] == 'R':
        o2 = (orientation - 1) % 4
    elif policy3D[orientation][x][y] == 'L':
        o2 = (orientation + 1) % 4
    x,y = [x,y] + np.array(forward[o2])
    orientation = o2
    policy2D[x][y] = policy3D[orientation][x][y]
    
print('policy 2d:')
print(policy2D)





###################
# output:
# policy 2d:
# [[' ' ' ' ' ' 'R' '#' 'R']
#  [' ' ' ' ' ' '#' ' ' '#']
#  ['*' '#' '#' '#' '#' 'R']
#  [' ' ' ' ' ' '#' ' ' ' ']
#  [' ' ' ' ' ' '#' ' ' ' ']]
###################
