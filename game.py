import pygame
import numpy as np
from CA import *
from neighborhood import *
from layer import *

class CAGame:

    def __init__(self, side : int, rule : CArule, window_size : int = 600, light_teme : bool = False):
        
        self.side = side
        self.rule = rule
        self.ca_layer = CA_layer(side, rule)
        self.path_layer = Path_layer(side, eyes = True)
        self.player_pos = np.array([0, 0], dtype=int)
        self.grid = np.zeros(shape = (side, side))
        self.reward_pos = np.array([side-1, side-1], dtype = int)
        self.count = 0
        # WINDOW SETTINGS
        self.window_size = window_size
        self.cell_dimension = self.window_size//side
        # COLOR SETTINGS
        self.light_theme = light_teme
        self.background_color = (0, 0, 0)
        self.line_color = (255, 255, 255)
        self.cell_color = (255, 255, 0)
        self.player_color = (255, 0, 0)
        self.reward_color = (0, 255, 0)
        # TECHNICAL SETTINGS
        self.fps = 60
    
    def update(self):
        self.ca_layer.update()
        self.path_layer.update()
        self.grid = self.ca_layer.get()*(1 - self.path_layer.get())
        self.grid[self.reward_pos[0], self.reward_pos[1]] = 0

    def reset(self):
        self.player_pos = np.array([0, 0])
        self.ca_layer.grid = self.ca_layer.initial_condition.copy()
        self.grid = np.zeros(shape=(self.side, self.side))
        self.reward_pos = np.array([self.side-1, self.side-1], dtype = int)
        self.count = 0

    def check_collision(self):
        return self.grid[self.player_pos[0], self.player_pos[1]] == 1 # True when player is on some alive cell (it can be in not-alive but shading cell) 
    
    def check_reward(self):
        return self.player_pos[0] == self.reward_pos[0] and self.player_pos[1] == self.reward_pos[1]
    
    def update_reward(self):
        self.reward_pos = np.random.randint(low = 0, high = self.side, size=(2))
    
    def update_player_pos(self, event : pygame.event):
        if event.key in (pygame.K_w, pygame.K_UP):
            if self.player_pos[0] > 0:
                self.player_pos[0] -= 1
        elif event.key in (pygame.K_s, pygame.K_DOWN):
            if self.player_pos[0] < self.side - 1:
                self.player_pos[0] += 1
        elif event.key in (pygame.K_a, pygame.K_LEFT):
            if self.player_pos[1] > 0:
                self.player_pos[1] -= 1
        elif event.key in (pygame.K_d, pygame.K_RIGHT):
            if self.player_pos[1] < self.side - 1:
                self.player_pos[1] += 1

    def render_grid(self, screen):
        for row in range(self.side):
            for column in range(self.side):
                x = column * self.cell_dimension
                y = row * self.cell_dimension
                k = self.grid[row, column]
                
                # light theme
                if self.light_theme:
                    shade = 255 if k == 1 else 255*(((self.rule.state + k + 1)/self.rule.state))
                    self.cell_color = (255, 255, 255) if k == 0 else (shade, shade, 255)
                # dark theme
                else:
                    shade = 255 if k == 1 else 255*(1 - ((self.rule.state + k + 1)/self.rule.state))
                    self.cell_color = (0, 0, 0) if k == 0 else (0, 0, shade)

                pygame.draw.rect(screen, self.cell_color, (x, y, self.cell_dimension, self.cell_dimension)) # questo è per la cella attuale
                #pygame.draw.rect(screen, line_color, (x, y, cell_dimension, cell_dimension), 1) # questo è per i bordi

    def render_player(self, screen):
        pygame.draw.rect(screen, self.player_color, (self.player_pos[1]*self.cell_dimension, self.player_pos[0]*self.cell_dimension, self.cell_dimension, self.cell_dimension))

    def render_reward(self, screen):
        pygame.draw.rect(screen, self.reward_color, (self.reward_pos[1]*self.cell_dimension, self.reward_pos[0]*self.cell_dimension, self.cell_dimension, self.cell_dimension)) # questo è per la cella attuale

    def play(self):
        
        self.reset()

        pygame.init()
        screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Cellular Automata Game")

        clock = pygame.time.Clock()

        running = True

        env_update_interval = 500  # ms → 1 update per second
        last_env_update = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.update_player_pos(event)

            if self.check_collision():
                print(f"You lose. You have scored {self.count}")
                pygame.quit()
                running = False

            if self.check_reward():
                self.update_reward()
                self.count += 1
                print(f"You win. Game will restart")
                self.reset()

            if running:
                
                now = pygame.time.get_ticks()
                if now - last_env_update >= env_update_interval: # It should do it once every second in this way
                    self.update()
                    last_env_update = now
                self.render_grid(screen)
                self.render_reward(screen)
                self.render_player(screen)                

                pygame.display.flip()

                clock.tick(self.fps)

        return 0

if __name__ == '__main__':
    rule = CArule([4], [1], 2, von_neighbourhood)
    c = CAGame(50, rule, light_teme=False)
    while True:
        c.play()
        choice = input("Play Again? y/n\n")
        if choice.lower() == 'n':
            break
    