from p5 import *
import math
import random
from settings import *

class Pipe:
    def __init__(self):
        self.width = pipeWidth
        self.height = floor(random.randrange(pipeLimit, height - pipeLimit - pipeGap))
        self.x = width
        self.y = self.height

    def show(self):
        stroke(0, 170, 0)
        fill(0, 170, 0)
        # text_size(32)
        text(str(self.height), self.x, self.y)
        rect(self.x, 0, self.width, self.height)
        rect(self.x, self.y + pipeGap, self.width, height)
    

    def update(self):
        self.x -= panSpeed
        self.show()

    def collided(self, bird):
        if bird.y + bird.sizeY >= height:
            return True
        if bird.x + bird.sizeX >= self.x and bird.x <= self.x + self.width:
            if bird.y + bird.sizeY >= self.y + pipeGap or bird.y <= self.y:
                return True
        return False