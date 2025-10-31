from particle import Particle
import pygame
import random
import math

pygame.init()

width, height = 2560, 1440
SCREEN = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("My Pygame Game")

running = True
clock = pygame.time.Clock()
FPS = 600

trail_surface = pygame.Surface((width, height))
trail_surface.set_alpha(0)

particles: list[Particle] = []

particlecount = 5000

for i in range(particlecount):
    particles.append(Particle.createParticle(width, height, xvel=1, size=1, colors=('Black', 'White')))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    SCREEN.blit(trail_surface, (0, 0))
    for particle in particles:
        
        particle.velocity.xy = particle.velocity.x*1.001, 1

        particle.position.x %= 2560
        particle.position.y %= 1440

        dx = abs(particle.position.x - 1280)
        dy = abs(particle.position.y - 720)

        particle.color = ((255,int((dx/1280)*255),0) if dx**2+dy**2<300**2 else (0,int((dy/720)*255),255))
        particle.draw(SCREEN)
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()