import sys
import pygame
from pygame import *
import math

class Ball:
    def __init__(self, x, y):
        self.length = ((x - origin.x)**2 + (y - origin.y)**2)**(1/2)
        self.angle = math.atan((x - origin.x) / (y - origin.y))
        self.x, self.y = x, y

        self.acc, self.vel = 0, 0
    
    def move(self):
        self.acc = - 0.5 * GRAVITY * math.sin(self.angle) / self.length 

        self.vel += self.acc
        self.angle += self.vel

        self.x, self.y = origin.x + math.sin(self.angle) * self.length, origin.y + math.cos(self.angle) * self.length

    def draw(self):
        pygame.draw.line(screen, (255, 255, 255), [origin.x, origin.y], [self.x, self.y])
        pygame.draw.circle(screen, (255, 255, 255), [self.x, self.y], RADIUS)

GRAVITY = 0.005
SCREEN_SIZE = 1000
RADIUS = 10

pygame.init()
pygame.time.Clock()
pygame.display.set_caption('Pendulum')
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

origin = Vector2(SCREEN_SIZE / 2, 0)

balls = []
balls.append(Ball(800, 1))

while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for ball in balls:
        ball.move()
        ball.draw()
        
    pygame.display.update()
