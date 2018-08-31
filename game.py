import pygame
import config

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
        
        if self.frameNum % config.PIPE_FREQUENCY == 0:
            # spawn new pipe
            print("added new pipe")
            newPipe = Pipe(250)
            self.currentPipes.append(newPipe)
        self.frameNum += 1
        
        
    def readInput(self, events):
        """
        Reads input from the user
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.birdVelocity = config.BIRD_VELOCITY
