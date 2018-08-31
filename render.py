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
        birdX = game.birdHorizontal
        birdY = game.birdHeight

        pygame.draw.rect(self.screen, RED, (
            birdX - config.BIRD_SIZE/2,
            birdY - config.BIRD_SIZE/2,
            config.BIRD_SIZE,
            config.BIRD_SIZE
        ))

        for pipe in game.currentPipes:
            pygame.draw.rect(self.screen, GREEN, (
                pipe.x,
                pipe.height,
                pipe.width,
                1000
            ))

        pygame.display.update()

