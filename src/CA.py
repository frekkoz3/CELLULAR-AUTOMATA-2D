import numpy as np
from neighborhood import *

class Rule:
    
    def __init__(self, alive, born, state, neighbourhood):
        self.alive = alive
        self.born = born
        self.state = state
        self.neighbourhood = neighbourhood

    def update_cell(self, grid, index):
        pass

    def update_grid(self, grid):
        pass

class CArule(Rule):

    def __init__(self, alive, born, state, neighbourhood):
        super().__init__(alive, born, state, neighbourhood)

    def update_cell(self, grid, index):
        if grid[index] == 1:
            if self.neighbourhood(grid, index) in self.alive:
                return 1
            else:
                return -self.state
        elif grid[index] == 0:
            if self.neighbourhood(grid, index) in self.born:
                return 1
            else:
                return 0
        else:
            return grid[index] + 1
        
    def update_grid(self, grid):
        side = len(grid)
        new_grid = np.zeros_like(grid)
        for i in range (side):
            for j in range(side):
                new_grid[i, j] = self.update_cell(grid, (i, j))
        return new_grid