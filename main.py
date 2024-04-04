#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving AI using Pygame & NEAT (neural networks)

import pygame
import neat
import os
import math
import sys

# We need to make a class, if we want each car to be an seperate object
class Car(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.image = pygame.image.load(os.path.join("Images", "car.png"))
        
        self.rect = self.image.get_rect(center=(490, 820))

        # Velocity vector
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0
        
        # Alive or not
        self.alive = True
        
        # each car will have up to 5 radars 
        self.radars = []


    # move forward  
    def drive(self):

        return

    def checkBorders():
        return
    



if __name__ == '__main__':
    print("Running Application")