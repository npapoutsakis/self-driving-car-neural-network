#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving RaceCar - AI using Pygame & NEAT (neural networks)

import pygame
import sys

from Car import RaceCar
from Utils import TRACK, SCREEN

# Init RaceCar
car = pygame.sprite.GroupSingle(RaceCar())

def eval_genomes():

    SCREEN.blit(TRACK, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    user_input = pygame.key.get_pressed()
    
    if sum(user_input) <= 1:
        car.sprite.isDriving = False
        car.sprite.direction_vector = 0

    if user_input[pygame.K_UP]:
        car.sprite.isDriving = True
    else:
        car.sprite.isDriving = False

    if user_input[pygame.K_RIGHT]:
        car.sprite.direction_vector = 1


    if user_input[pygame.K_LEFT]:
        car.sprite.direction_vector = -1

    # Update car position and rotation
    car.update()

    # Render
    car.draw(SCREEN)
    
    # Update display
    pygame.display.update()


# Run application
if __name__ == "__main__":
    pygame.init()  # Initialize Pygame

    # main()
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running flag to False to exit the loop
        # Evaluate genomes and update game state
        eval_genomes()

    pygame.quit()  # Quit Pygame properly
    sys.exit()  # Exit the script

