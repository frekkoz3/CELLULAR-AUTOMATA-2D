import numpy as np

def moore_neighbourhood(grid, index):
    y = index[0]
    x = index[1]

    side = len(grid)
    moore = []
    for i in range(y-1, y+2):
        k = i%side
        row = []
        for j in range (x-1, x + 2):
            w = j%side
            row.append(grid[k, w])
        moore.append(row)
    
    moore = np.array(moore)
    offset = 1 if grid[index] !=0 else 0 # non dobbiamo considerare la cellula stessa
    return np.count_nonzero(moore) - offset 

def von_neighbourhood(grid, index):
    y = index[0]
    x = index[1]

    side = len(grid)
    von = []
    
    for i in range (y-1, y+2):
        k = i%side
        if y != k:
            von.append(grid[k, x])
    
    for j in range (x-1, x+2):
        w = j%side
        if x != w:
            von.append(grid[y, w])
    
    von = np.array(von)
    return np.count_nonzero(von)

def diag_neighbourhood(grid, index):
    return moore_neighbourhood(grid, index) - von_neighbourhood(grid, index)