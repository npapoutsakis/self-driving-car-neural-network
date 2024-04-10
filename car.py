import pygame
import math

from Utils import SCREEN, CAR_IMAGE

class RaceCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car_image = CAR_IMAGE
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
        self.alive = True
    
    # Updating 
    def update(self):
        self.drive()
        self.rotate()
        
        # draw sensors
        for sensor_angle in (-60, -30, 0, 30, 60):
            self.sensor(sensor_angle)

        self.collision()

    # Move the car forward
    def drive(self):
        if self.isDriving:
            self.rect.center += self.velocity_vector * 6

    # Rotate car image and update
    def rotate(self):
        if self.direction_vector == 1:
            self.angle -= self.rotation_vector
            self.velocity_vector.rotate_ip(self.rotation_vector)
        if self.direction_vector == -1:
            self.angle += self.rotation_vector
            self.velocity_vector.rotate_ip(-self.rotation_vector)

        self.image = pygame.transform.rotozoom(self.car_image, self.angle, 0.08)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    # Sensors
    def sensor(self, sensor_angle):

        # length of the sensor
        length = 0

        # center of the race car
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        # until it reaches the green area
        while not SCREEN.get_at((x, y)) == pygame.Color(0, 150, 75, 255) and length < 200:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + sensor_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + sensor_angle)) * length)

        # Draw sensors
        pygame.draw.line(SCREEN, (255, 102, 102, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (x, y), 3)
    

    # If the front hits the grass, we reset
    def collision(self):
        length = 30

        # points to hit
        collision_point_right = [int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
                                 int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)]

        collision_point_left = [int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
                                int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)]

        # Die on Collision
        if SCREEN.get_at(collision_point_right) == pygame.Color(0, 150, 75, 255) \
                or SCREEN.get_at(collision_point_left) == pygame.Color(0, 150, 75, 255):
            self.alive = False

        # Draw Collision Points
        pygame.draw.circle(SCREEN, (0, 0, 0, 0), collision_point_right, 5)
        pygame.draw.circle(SCREEN, (0, 0, 0, 0), collision_point_left, 5)