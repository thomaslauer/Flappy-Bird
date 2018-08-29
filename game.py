import pygame
import config

class Pipe:
    def __init__(self, height):
        self.height = height
        self.x = 1


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

        # the amount to move the frames by
        self.window_speed = 0.01
    
    def nextFrame(self):
        self.birdVelocity += config.GRAVITY
        self.birdHeight += self.birdVelocity
        """
        move pipes by window speed
        move bird by birdVelocity
        check if a pipe is out of the window, remove it
        check for collisions with player
        read input from player (jump y/n)
        spawn new pipes if needed
        """
    
    def readInput(self, events):
        """
        Reads input from the user
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.birdVelocity = config.BIRD_VELOCITY
