import time
import pygame
import config
import game

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
        self.screen = pygame.display.set_mode((config.WINDOW_SIZE, config.WINDOW_SIZE))

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

    def draw(self, game):
        # fill screen with black to clear
        self.screen.fill(BLACK)

        # draw bird

        birdRect = (game.birdHorizontal, game.birdHeight, config.BIRD_SIZE, config.BIRD_SIZE)

        pygame.draw.rect(self.screen, RED, birdRect)

        for pipe in game.currentPipes:
            upperPipeRect = (pipe.x, pipe.height + pipe.gap/2, pipe.width, 1000)
            lowerPipeRect = (pipe.x, 0, pipe.width, pipe.height - pipe.gap/2)
            
            pygame.draw.rect(self.screen, GREEN, upperPipeRect)
            pygame.draw.rect(self.screen, GREEN, lowerPipeRect)

        pygame.display.update()

        