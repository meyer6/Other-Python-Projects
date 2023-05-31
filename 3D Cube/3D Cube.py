import sys
import pygame
from pygame import *
import numpy as np
import math

# Defines the cubes' vertices
points = np.array([[0, 0, 0], [0, 200, 0], [0, 0, 200], [200, 0, 0], [0, 200, 200], [200, 200, 0], [200, 0, 200], [200, 200, 200]])
points2 = []

# Defines the connections between vertices
edges = np.array([[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 4], [2, 6], [3, 5], [3, 6], [7, 6], [7, 5], [7, 4]])

# Defines angles of camera (Just used to make camera rotate)
x1 = 1
x2 = 1

# Sets up pygame
SCREEN_SIZE = 600
pygame.init()
pygame.display.set_caption('Cube')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# moving = False
while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == MOUSEBUTTONDOWN:  
        #     moving = True
        #     startAngles = [x1, x2]
        #     startCoords = pygame.mouse.get_pos()

        # if event.type == MOUSEMOTION and moving:
        #     pos = pygame.mouse.get_pos()
        #     x1 = startAngles[0] + (startCoords[0] - pos[0]) / 250
        #     x2 = startAngles[1] + (startCoords[1] - pos[1]) / 250

        # if event.type == MOUSEBUTTONUP:
        #     moving = False

    # Makes background black
    screen.fill((0, 0, 0))
    
 
    # Rotates camera and camera angle (Just used to make camera rotate)
    dt = clock.tick(60) / 1000  
    x1 += dt * 0.15
    x2 += dt * 0.2

    x = math.cos(x2) * math.cos(x1)
    y = math.sin(x2)
    z = math.cos(x2) * math.sin(x1)
    # print(x**2 + y**2 + z**2)
    # z = (1 - y**2 - x**2)**(1/2)
    
    rotation = np.array([x, y, z])
    camera = rotation * -1000 + 100


    # https://math.stackexchange.com/questions/114512/how-to-find-the-orthonormal-transformation-that-will-rotate-a-vector-to-the-x-ax?rq=1
    # Calculates the inverse of the change in basis matrix
    theta = math.atan(- rotation[2] / rotation[1])
    alpha = math.atan(- (math.cos(theta) * rotation[1] - math.sin(theta) * rotation[2]) / rotation[0])

    newBase = np.array([[math.cos(alpha), - math.sin(alpha) * math.cos(theta), math.sin(alpha) * math.sin(theta)], 
            [math.sin(alpha), math.cos(alpha) * math.cos(theta),  - math.cos(alpha) * math.sin(theta)], 
            [0, math.sin(theta), math.cos(theta)]]) 
    

    for point in points:
        # Translates the point to make the camera the centre
        newPoint = point - camera 

        # Calculates the vector to the point in the new rotated space
        coords = newBase.dot(newPoint)

        # coords[0] = abs(coords[0])
        points2.append(coords)

        #print(coords[0])
        # Draws point
        pygame.draw.circle(screen, (255, 255, 255), [SCREEN_SIZE // 2 + coords[1] / coords[0] * 750, SCREEN_SIZE // 2 + coords[2] / coords[0] * 750], 5) 

    # Draws edges
    for edge in edges:            
        pygame.draw.line(screen, (255, 255, 255), [SCREEN_SIZE // 2 + points2[edge[0]][1] / points2[edge[0]][0] * 750, SCREEN_SIZE // 2 + points2[edge[0]][2] / points2[edge[0]][0] * 750], 
                         [SCREEN_SIZE // 2 + points2[edge[1]][1] / points2[edge[1]][0] * 750, SCREEN_SIZE // 2 + points2[edge[1]][2] / points2[edge[1]][0] * 750])
    points2 = []


    pygame.display.update()






    #     pygame.draw.circle(screen, (255, 255, 255), [SCREEN_SIZE // 2 + coords[1] / coords[0]**(1/3) * 7.5, SCREEN_SIZE // 2 + coords[2] / coords[0]**(1/3) * 7.5], 5) 

    # # Draws edges
    # for edge in edges:
    #     pygame.draw.line(screen, (255, 255, 255), [SCREEN_SIZE // 2 + points2[edge[0]][1] / points2[edge[0]][0]**(1/3) * 7.5, SCREEN_SIZE // 2 + points2[edge[0]][2] / points2[edge[0]][0]**(1/3) * 7.5], 
    #                      [SCREEN_SIZE // 2 + points2[edge[1]][1] / points2[edge[1]][0]**(1/3) * 7.5, SCREEN_SIZE // 2 + points2[edge[1]][2] / points2[edge[1]][0]**(1/3) * 7.5])
    # points2 = []













        # if rotation[1] == 0:
        #     x = 0

        # Ryz = np.array([[1, 0, 0],
        #                 [0, math.cos(x), -math.sin(x)],
        #                 [0, math.sin(x), math.cos(x)]])
        

        # x = math.atan( - rotation[1] / rotation[0])
        # if rotation[0] == 0:
        #     x = 0
        
        # Rxy = np.array([[math.cos(x), -math.sin(x), 0], 
        #                 [math.sin(x), math.cos(x), 0],
        #                 [0, 0, 1]])
        

    

        # axisRotationMatrix = np.matmul(Rxy, Ryz)

        # print(axisRotationMatrix)

        # Calculates transformation matrix to rotate axis
        # newBase = Rxy # np.linalg.inv(axisRotationMatrix) #np.array([[rotation[0], -rotation[1]], [rotation[1], rotation[0]]]))











# import sys
# import pygame
# from pygame import *
# import numpy as np


# WHITE = (255, 255, 255)
# WIDTH = 500
# HEIGHT = 500

# pygame.init()
# display = pygame.display
# surface = display.set_mode((WIDTH, HEIGHT))
# display.set_caption("3D")


# points = np.array([[50, 50], [100, 50]])
# # points = (
# #     ( 50,  50,  50),
# #     (-50,  50,  50),
# #     ( 50, -50,  50),
# #     ( 50,  50, -50),
# #     (-50,  50, -50),
# #     ( 50, -50, -50),
# #     (-50, -50, -50),
# #     (-50, -50,  50),
# # )
# camera = np.array([75, 0])
# rotation = np.array([0, 1])

# SCREEN_SIZE = 1000

# pygame.init()
# pygame.time.Clock()
# pygame.display.set_caption('Pendulum')
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))


# while True :
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill((0, 0, 0))

#     for point in points:
#         # Translates all points to make the camera the centre
#         newPoint = point - camera 

#         # Calculates transformation matrix to rotate axis
#         newBase = np.linalg.inv(np.array([[rotation[0], -rotation[1]], [rotation[1], rotation[0]]]))

#         # Calculates the vector from the camera to the point in the new rotated system
#         coords = newBase.dot(newPoint)

#         # Draws point
#         pygame.draw.circle(screen, (255, 255, 255), [SCREEN_SIZE // 2 + coords[1], SCREEN_SIZE // 2], 5) # // coords[0] * 100


#     pygame.display.update()