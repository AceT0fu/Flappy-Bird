from p5 import *
import settings
from bird import Bird

class Game:
    time = 0
    dead = False

    birds = []
    pipes = []

    initialJumpInt = 8

# def setup():
#     size(settings.width, settings.height)

#     for x in range(settings.birdNo):
#         birds.append(Bird(0, 0))
        

# def draw():
#     # setup background and floor
#     background(120, 220, 220)
#     stroke(0, 220, 100)
#     fill(0, 220, 100)
#     rect(0, settings.height - settings.floorH, settings.width, settings.floorH)

#     settings.t += 1

# run()