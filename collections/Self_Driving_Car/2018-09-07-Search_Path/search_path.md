# Search



- [Search](#search)
    - [first search](#first-search)
    - [expansion grid](#expansion-grid)
    - [print path](#print-path)
    - [A-star](#a-star)
    - [dynamic programming - value](#dynamic-programming---value)
    - [dynamic programming - policy](#dynamic-programming---policy)
    - [dynamic programming - policy for 3-values state](#dynamic-programming---policy-for-3-values-state)



## first search

- result: reached goal [4,5] after 11 steps
``` py
[11, 4, 5]
```
- [code](./ref/0_first_search.py)


## expansion grid
- result: the order of expansion
``` py
[[  0,   1,  -1,  11,  15,  18],
 [  1,   3,   5,   8,  12,  16],
 [  4,   6,  -1,  13,  -1,  19],
 [  7,   9,  -1,  17,  -1,  21],
 [ 10,  14,  -1,  20,  -1,  22]]
```
- [code](./ref/1_expansion_grid.py) 






## print path
- result: showing path
``` py
[['>' 'v' ' ' ' ' ' ' ' ']
 [' ' '>' '>' '>' '>' 'v']
 [' ' ' ' ' ' ' ' ' ' 'v']
 [' ' ' ' ' ' ' ' ' ' 'v']
 [' ' ' ' ' ' ' ' ' ' '*']]
```
- [code](./ref/2_print_path.py)



## A-star
- result: faster for path finding
``` py
[[ 0 -1 10 11 12 -1]
 [ 1 -1  9 -1 13 -1]
 [ 2 -1  8 -1 14 -1]
 [ 3 -1  7 -1 15 16]
 [ 4  5  6 -1 -1 17]]
```
- [code](./ref/3_A_star.py)





## dynamic programming - value
- result: get values of every state
``` py
[[11. 99.  7.  6.  5.  4.]
 [10. 99.  6.  5.  4.  3.]
 [ 9. 99.  5.  4.  3.  2.]
 [ 8. 99.  4.  3.  2.  1.]
 [ 7.  6.  5.  4. 99.  0.]]
```
- [code](./ref/4_dynamic_programming_value.py) 


## dynamic programming - policy
- resutl: got policy for every state
``` py
[['v' ' ' 'v' 'v' 'v' 'v']
 ['v' ' ' 'v' 'v' 'v' 'v']
 ['v' ' ' 'v' 'v' 'v' 'v']
 ['v' ' ' '>' '>' '>' 'v']
 ['>' '>' '^' '^' ' ' '*']]
```
- [code](./ref/5_dynamic_programming_policy.py)



## dynamic programming - policy for 3-values state
- result: from policy (orientaion, x, y) to get a 2d solution (x, y) and (action) for current state
``` py
policy 2d:
[[' ' ' ' ' ' 'R' '#' 'R']
 [' ' ' ' ' ' '#' ' ' '#']
 ['*' '#' '#' '#' '#' 'R']
 [' ' ' ' ' ' '#' ' ' ' ']
 [' ' ' ' ' ' '#' ' ' ' ']]
```
- [code](./ref/6_dynamic_programming_policy_for_3_values_state.py)