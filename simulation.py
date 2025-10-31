from particle import Particle
import pygame

pygame.init()

width, height = 2560, 1440
SCREEN = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("My Pygame Game")

running = True
clock = pygame.time.Clock()
FPS = 600

trail_surface = pygame.Surface((width, height))
trail_surface.set_alpha(255)

particles: list[Particle] = []

particlecount = 150

for i in range(particlecount):
    particles.append(Particle.createParticle(width, height, size=4))

while running:
    SCREEN.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for particle in particles:
        total_force = pygame.Vector2()
        for otherparticle in particles:
            if particle is otherparticle:
                continue

            dx, dy = Particle.toro(particle, otherparticle, width, height)
            offset = pygame.Vector2(dx, dy)
            dist = offset.length()

            if dist == 0:
                continue

            direction = offset.normalize()
            
            if 1 < dist < particle.size*2:
                total_force -= direction * (5 / dist)

            total_force += direction * (0.3 / dist)

        particle.velocity += total_force
        particle.velocity *= 0.9
        particle.position += particle.velocity

        particle.position.x %= width
        particle.position.y %= height

        particle.draw(SCREEN)

    pygame.display.flip()

pygame.quit()
