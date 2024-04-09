#   Autonomous Agents Project 2023
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving AI using Pygame & NEAT (neural networks)

import pygame
import neat
import os
import math
import sys

# Track dimensions
WINDOW_HEIGHT = 564
WINDOW_WIDTH = 696

# Main Function
def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   
    clock = pygame.time.Clock()
    track = pygame.image.load("track.png")
    car = pygame.image.load("car.png")
    
    running = True

    # While the application is running, do not close window
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Rendering the application here
        screen.blit(track, (0, 0))

        


            
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    return 



# Run
if __name__ == "__main__":
    main()