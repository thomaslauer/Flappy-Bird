import pygame
import config
import util

from random import randint

class Pipe:
    def __init__(self, height):
        self.height = height
        self.width = config.PIPE_SIZE
        self.x = config.WINDOW_SIZE
        self.gap = config.WINDOW_SIZE / 3
    
    def move(self, amount):
        self.x -= amount


class Game:
    """
    Holds and updates the game's state
    """

    def __init__(self):
        # define the position and velocity of the bird
        self.birdHeight = config.WINDOW_SIZE/2
        self.birdHorizontal = config.WINDOW_SIZE/5
        self.birdVelocity = 0

        # define a list of currently visible pipes
        self.currentPipes = []

        self.frameNum = 0
        self.jump = 0
    
    def nextFrame(self):
        """
        move pipes by window speed
        move bird by birdVelocity
        check if a pipe is out of the window, remove it
        check for collisions with player
        read input from player (jump y/n)
        spawn new pipes if needed
        """
        self.birdVelocity += config.GRAVITY
        self.birdHeight += self.birdVelocity

        for pipe in self.currentPipes:
            pipe.move(config.PIPE_SPEED)
        
        self.checkCollisions()

        if self.frameNum % config.PIPE_FREQUENCY == 0:
            # spawn new pipe
            newPipe = Pipe(randint(100, 400))
            self.currentPipes.append(newPipe)
        self.frameNum += 1
        
        
    def readInput(self, events):
        self.jump = 0
        """
        Reads input from the user
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.birdVelocity = config.BIRD_VELOCITY
                    self.jump = 1

    def checkWindowCollisions(self):
        """
        Detects collisions with the top or bottom of the frame
        """
        if self.birdHeight < 0 or self.birdHeight + config.BIRD_SIZE > config.WINDOW_SIZE:
            return True
        return False

    def checkCollisions(self):
        birdRect = (self.birdHorizontal, self.birdHeight, config.BIRD_SIZE, config.BIRD_SIZE)

        for pipe in self.currentPipes:
            upperPipeRect = (pipe.x, 0, pipe.width, pipe.height - pipe.gap/2)
            lowerPipeRect = (pipe.x, pipe.height + pipe.gap/2, pipe.width, 1000)

            if util.checkCollide(birdRect, upperPipeRect):
                return True
            if util.checkCollide(birdRect, lowerPipeRect):
                return True
        return False
    
    def writeCSV(self, writer):
        data = dict()

        data['frameNum'] = self.frameNum

        if len(self.currentPipes) < 2:
            data['distToPipe'] = self.currentPipes[-1].x
        else:
            data['distToPipe'] = self.currentPipes[-2].x

        data['birdY'] = self.birdHeight
        data['birdV'] = self.birdVelocity
        data['jump'] = self.jump

        writer.writerow(data)
