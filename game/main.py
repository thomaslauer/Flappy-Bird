import pygame
import csv
import os
from render import Window
from game import Game

fieldnames = ['frameNum', 'distToPipe', 'birdY', 'birdV', 'jump']

def main():
    game = Game()
    display = Window()
    display.setup()

    with open('log.csv', mode='a') as csvFile:

        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        #writer.writeheader()
        run = True
        while run:
            currentFrameData = dict()

            print(game.frameNum)
            if game.frameNum != 0:
                game.writeCSV(writer)

            pygame.time.delay(int(1000/60))
            events = pygame.event.get()
            game.readInput(events)
            game.nextFrame()
            display.draw(game)


            if game.checkCollisions():
                game = Game()
            if game.checkWindowCollisions():
                game = Game()

            for event in events:
                if event.type == pygame.QUIT:
                    run = Fals
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

main()
