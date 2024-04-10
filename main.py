#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving RaceCar - AI using Pygame & NEAT (neural networks)

import pygame
import sys
import neat
import math

from Car import RaceCar

# Game basics
TRACK = pygame.image.load("Images/track.png")

# Setup window
SCREEN =  pygame.display.set_mode((TRACK.get_width(), TRACK.get_height()))

# Init RaceCars
car = pygame.sprite.GroupSingle(RaceCar())

def eval_genomes():

    SCREEN.blit(TRACK, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




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

