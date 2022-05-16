import pygame
from sys import exit
from random import randint, choice


class ParticlePrinciple:
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(screen, pygame.Color(choice(colors)), particle[0], int(particle[1]))

    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = randint(10, 15)
        direction_x = randint(-5, 5)
        direction_y = randint(-5, 5)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


clock = pygame.time.Clock()

colors = ['green', 'blue', 'pink', 'purple', 'white']
colors2 = ['grey10', 'grey20', 'grey30', 'grey40', 'grey50', 'grey60', 'grey70', 'grey80', 'grey90']

bg_color = 'white'

pygame.init()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 25)

# Screen stuff
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Particles')

while True:

    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()

    particle1.emit()

    pygame.display.update()
    clock.tick(120)

