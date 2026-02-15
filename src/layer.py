import numpy as np
import pygame 
from neighborhood import *
from CA import *

class layer:

    def __init__(self, side : int):
        self.side = side
        self.grid = np.zeros(shape=(side, side))

    def init_interface(self):
        pygame.init()

        window_size = 600
        cell_dimension = window_size//self.side
        background_color = (0, 0, 0)
        line_color = (255, 255, 255)

        fps = 60

        screen = pygame.display.set_mode((window_size, window_size))
        pygame.display.set_caption("Cellular Automata - Setup")

        clock = pygame.time.Clock()

        running = True

        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos[0]//cell_dimension, event.pos[1]//cell_dimension
                    if 0 <= x < self.side and 0 <= y < self.side:
                        self.grid[y, x] = 0 if self.grid[y, x] == 1 else 1
            
            if running:

                screen.fill(background_color)

                for row in range(self.side):
                    for column in range(self.side):
                        x = column * cell_dimension
                        y = row * cell_dimension
                        cell_color = (0, 0, 0) if self.grid[row, column] == 0 else (255, 255, 255)
                        pygame.draw.rect(screen, cell_color, (x, y, cell_dimension, cell_dimension)) # questo è per la cella attuale
                        #pygame.draw.rect(screen, line_color, (x, y, cell_dimension, cell_dimension), 1) # questo è per i bordi

                pygame.display.flip()

                clock.tick(fps)

    def get(self):
        return self.grid
    
    def update(self):
        pass

class CA_layer(layer):

    def __init__(self, side : int, rule : CArule):
        super().__init__(side)
        self.init_interface()
        self.initial_condition = self.grid.copy()
        self.rule = rule
        
    def update(self):
        self.grid = self.rule.update_grid(self.grid)
    
class Path_layer(layer):

    def __init__(self, side, eyes : bool = True):
        super().__init__(side)
        if not eyes:
            self.init_interface()
        else:
            self.grid = np.eye(self.side)
        self.initial_condition = self.grid.copy()

