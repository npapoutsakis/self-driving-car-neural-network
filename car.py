#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving RaceCar - AI using Pygame & NEAT (neural networks)

import pygame

class RaceCar(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.car_image = pygame.image.load("car.png")
        self.image = self.car_image

        # Starting position on grid
        self.rect = self.image.get_rect(center=(430, 90))

        # 
        self.velocity = pygame.math.Vector2(0.5, 0)
        self.isDriving = False
        self.angle = 0  
    
    def update(self):
        self.drive()
        self.rotate()
        

    def drive(self):
        

        return

    def rotate(self):
        
        return