import pygame

class RaceCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car_image = pygame.image.load("Images/car.png")
        self.image = self.car_image
        
        # Scale down car image
        # self.image = pygame.transform.scale(self.car_image, (50, 50))

        # Starting position on grid
        self.rect = self.image.get_rect(center=(430, 90))

        # Movement  
        self.velocity_vector = pygame.math.Vector2(0.8, 0)
        self.direction_vector = 0
        self.angle = 0
        self.rotation_vector = 5

        # flag
        self.isDriving = False

    
    # Updating 
    def update(self):
        self.drive()
        self.rotate()

    # Move the car forward
    def drive(self):
        if self.isDriving:
            self.rect.center += self.velocity_vector * 6

    # Rotate car image and update
    def rotate(self):
        if self.direction_vector == 1:
            self.angle -= self.rotation_vector
            self.vel_vector.rotate_ip(self.rotation_vector)
        if self.direction_vector == -1:
            self.angle += self.rotation_vector
            self.vel_vector.rotate_ip(-self.rotation_vector)

        self.image = pygame.transform.rotozoom(self.car_image, self.angle, 0.08)
        self.rect = self.image.get_rect(center=self.rect.center)