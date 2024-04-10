#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving RaceCar - AI using Pygame & NEAT (neural networks)

import pygame
import sys
import os
import neat
import math

from Car import RaceCar

# Track dimensions
WINDOW_WIDTH = 1212
WINDOW_HEIGHT = 682

# Game basics
SCREEN =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TRACK = pygame.image.load(os.path.join("Images", "track.png"))

car = pygame.sprite.GroupSingle(RaceCar())

def eval_genomes():
    SCREEN.blit(TRACK, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    user_input = pygame.key.get_pressed()

    # Update car position and rotation based on user input
    if user_input[pygame.K_UP]:
        car.sprite.isDriving = True
    else:
        car.sprite.isDriving = False

    # Update car position and rotation
    car.update()

    # Render
    car.draw(SCREEN)
    pygame.display.update()


# Run application
if __name__ == "__main__":
    pygame.init()  # Initialize Pygame

    # main()
    running = True
    while running:
        # Evaluate genomes and update game state
        eval_genomes()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Set running flag to False to exit the loop

    pygame.quit()  # Quit Pygame properly
    sys.exit()  # Exit the script

