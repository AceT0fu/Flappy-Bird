from p5 import *
import random
import pygame
import neat

from bird import Bird
from pipe import Pipe
from game import Game
from settings import *

pygame.init()
death = pygame.mixer.Sound("death.mp3")

# height = 800
# width = 800

# floorH = 200

# panSpeed = 4
# gravity = 0.8
# gap = 225
# jump = 12
# pipeLimit = 250

# birdNo = 10

game = Game()


def setup():
    size(width, height)
    
    for x in range(birdNo):
        game.birds.append(Bird(50 + x * 50, height / 2))

    game.pipes.append(Pipe())
        

def draw():
    # setup background and floor
    background(120, 220, 220)
    stroke(0, 220, 100)
    fill(0, 220, 100)
    rect(0, height - floorH, width, floorH)

    game.time += 1

    # update pipes
    for pipe in game.pipes:
        pipe.update()

    # update birds
    for bird in game.birds:
        #decide whether to flap
        rand = random.randrange(100)
        if (rand < game.initialJumpInt):
            bird.flap()

        bird.update()

        # check death
        if (game.pipes[0].collided(bird)):
            game.birds.remove(bird)
            pygame.mixer.Sound.play(death)

    if game.pipes[len(game.pipes) - 1].x < width / 2:
        game.pipes.append(Pipe())

    if game.pipes[0].x + game.pipes[0].width < 0:
        del game.pipes[0]


# Set configuration file
configPath = "./config-feedforward.txt"
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation, configPath)
 
# Create the population, which is the top-level object for a NEAT run
p = neat.Population(config)

# Add a stdout reporter to show progress in the terminal
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

# p.run(eval_genomes, 10)

run()