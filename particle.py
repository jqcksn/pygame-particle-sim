import pygame
import random

class Particle:

    def __init__(self, position:tuple, velocity:tuple, color:tuple=(255,0,255), size:int=3) -> None:
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.color = pygame.Color(color)
        self.size = size

    def draw(self, screen):
        self.position += self.velocity
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.size)

    def createParticle(wid=0, hei=0, xpos=0, ypos=0, xvel=0, yvel=0, size=3, colors=False):
        if not (xpos or ypos):
            xpos=random.randint(0,wid)
            ypos=random.randint(0,hei)
        if not colors:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            color = random.choice(colors)
        return Particle((xpos, ypos), (xvel,yvel), color, size)

