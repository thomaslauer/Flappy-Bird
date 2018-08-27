import time

import pygame

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED  =  (255, 0,   0)
GREEN = (0,   255, 0)
BLUE =  (0,   0,   255)

class Window:
    def __init__(self):
        self.screen = None

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))

    def testDisplay(self):
        x = 0
        run = True
        while run:
            pygame.time.delay(int(1000/60))
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            pygame.draw.rect(self.screen, GREEN, (x, x, 100, 100))
            pygame.display.update()
            x += 1
