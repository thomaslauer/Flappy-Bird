
import pygame
from render import Window
from game import Game

def main():
    game = Game()
    display = Window()
    display.setup()

    run = True
    while run:
        pygame.time.delay(int(1000/60))
        events = pygame.event.get()
        game.readInput(events)
        game.nextFrame()
        display.draw(game)


        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

main()