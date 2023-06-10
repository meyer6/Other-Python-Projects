import sys
import pygame
from pygame import *
import random

def midPoint(arr1, arr2):
    return [(arr1[0] + arr2[0]) / 2, (arr1[1] + arr2[1]) / 2]

SCREEN_SIZE = 600
pygame.init()
pygame.display.set_caption('Fractal')
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

points = [[50, 50], [50, 550], [550, 300]]
points2 = [midPoint(points[0], points[1])]
for _ in range(10000):
    points2.append(midPoint(points2[-1], random.choice(points)))

while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    for point in points:
        pygame.draw.circle(screen, (255, 0, 0), [point[0], point[1]], 5) 

    for point in points2:
        pygame.draw.circle(screen, (255, 255, 255), [point[0], point[1]], 1) 

    pygame.display.update()





