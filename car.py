#   Autonomous Agents Project 2024
#       Nikolaos Papoutsakis
#           2019030206

import pygame, math

from utils import SCREEN, CAR_IMAGE

# Class that will represent our car model
class RaceCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car_image = CAR_IMAGE
        self.image = self.car_image

        # Scale down car image
        # self.image = pygame.transform.scale(self.car_image, (50, 50))        

        # Starting position on grid
        self.rect = self.image.get_rect(center=(505, 195))
        
        # Movement
        self.velocity_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vector = 5
        self.direction_vector = 0

        # flag
        self.alive = True

        # Sensors
        self.sensors = []

  
    # Updating state on each iteration
    def update(self):

        # erase sensor data each time the car moves
        self.sensors.clear()

        # Perform movement
        self.drive()
        self.rotate()

        # each sensor will have a specific angle
        for sensor_angle in (-60, -30, 0, 30, 60):
            self.sensor(sensor_angle)
        
        # Update collision data of sensors
        self.collision()

        # get distance from the tip of the sensor
        self.getSensorData()
        return

    # Move the car forward
    def drive(self):
        self.rect.center += self.velocity_vector * 5

    # If the front hits the grass, we reset
    def collision(self):
        length = 40
        
        # points to hit
        collision_r = [int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
                                 int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)]
        
        collision_l = [int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
                                int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)]

        # reset if collided
        if SCREEN.get_at(collision_r) == pygame.Color(0, 150, 75, 255) or SCREEN.get_at(collision_l) == pygame.Color(0, 150, 75, 255):
            self.alive = False

        # draw collision points
        pygame.draw.circle(SCREEN, (0, 255, 255, 0), collision_l, 4)
        pygame.draw.circle(SCREEN, (0, 255, 255, 0), collision_r, 4)
        
        return

    # rotation of the car
    def rotate(self):
        if self.direction_vector == 1:
            self.angle -= self.rotation_vector
            self.velocity_vector.rotate_ip(self.rotation_vector)
        if self.direction_vector == -1:
            self.angle += self.rotation_vector
            self.velocity_vector.rotate_ip(-self.rotation_vector)

        self.image = pygame.transform.rotozoom(self.car_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        return

    # create sensor
    def sensor(self, sensor_angle):
        # length of the sensor (line)
        length = 0

        # center of the race car
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])
        
        # until it reaches the green area
        while not SCREEN.get_at((x, y)) == pygame.Color(0, 150, 75, 255) and length < 200:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + sensor_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + sensor_angle)) * length)

        # draw the sensor
        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (x, y), 3)
        pygame.draw.line(SCREEN, (255, 255, 255, 255), self.rect.center, (x, y), 1)

        distance = int(math.sqrt(math.pow(self.rect.center[0] - x, 2)
                             + math.pow(self.rect.center[1] - y, 2)))

        self.sensors.append([sensor_angle, distance])
        
        return

    # Get distance info from sensors
    def getSensorData(self):
        input = [0, 0, 0, 0, 0]

        # each element will be the distance from the wall
        for i, sensor in enumerate(self.sensors):
            input[i] = int(sensor[1])
        return input