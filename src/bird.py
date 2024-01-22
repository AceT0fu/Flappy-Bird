from p5 import *
import math
from settings import *
import pygame

class Bird:
  def __init__(self, x, y):
    global panSpeed

    self.x = x
    self.y = y
    self.velX = panSpeed
    self.velY = 0
    self.sizeX = 80
    self.sizeY = 100
    self.roatation = - math.pi / 6
    
    self.topDist = 0
    self.botDist = 0
    self.time = 0

    self.image = load_image("tofu.PNG")
    self.boing = pygame.mixer.Sound("boing.mp3")


  def show(self):
    image(self.image, -self.sizeX / 2, -self.sizeY / 2, self.sizeX, self.sizeY)

  def update(self):
    self.time += 1

    # fall with gravity
    self.velY += gravity
    self.y += self.velY

    # hit the ceiling
    if self.y <= 0:
        self.y = 0
        self.velY = 0

    # hit the floor
    if self.y + self.sizeY >= height - floorH:
      self.velY = - self.velY

    # gravity rotation
    with push_matrix():
      translate(self.x + self.sizeX / 2, self.y + self.sizeY / 2)

      if self.velY < 5:
        rotate(- math.pi / 4)
        self.rotation = - math.pi / 6
      elif self.velY <= 15: 
        self.rotation += math.pi / 14
        self.rotation = constrain(self.rotation, -math.pi / 4, math.pi / 2)
        rotate(self.rotation)
      else:
        rotate(math.pi / 2)

      self.show()

  def flap(self):
    self.velY = -jump
    pygame.mixer.Sound.play(self.boing)