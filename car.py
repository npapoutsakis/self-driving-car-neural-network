import pygame
import os

class RaceCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Images", "car.png"))
        self.image = self.image = pygame.transform.scale(self.original_image, (50, 50))

        # Starting position on grid
        self.rect = self.image.get_rect(center=(430, 90))

        # Movement
        self.velocity_vector = pygame.math.Vector2(0.4, 0)
        self.direction_vector = 0

        self.isDriving = False
    
    # Updating 
    def update(self):
        self.drive()
        self.rotate()

    # Move the car forward
    def drive(self):
        if self.isDriving:
            self.rect.center += self.velocity_vector * 3

    # Rotate car image and update
    def rotate(self):
        return