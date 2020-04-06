#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com
# Copy you Sudo in grid line by line like this and replace the unknowns numbers by 0
# Here the grid is 9 and 9. Modify the ranges if your grid is bigger or smaller

import numpy as np

grid = [
    [2,5,0,0,0,0,0,0,7],
    [0,0,0,0,4,7,0,0,5],
    [0,0,9,3,0,5,8,0,0],
    [0,2,7,5,0,4,9,0,0],
    [0,9,0,0,0,0,0,8,0],
    [0,0,1,9,0,3,5,4,0],
    [0,0,6,7,0,8,3,0,0],
    [5,0,0,1,3,0,0,0,0],
    [7,0,0,0,0,0,0,6,8],
]


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[y0 + i][x0 + j] == n:
                    return False
    return True


def solver():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solver()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More solution ?")


solver()
