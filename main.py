#   Autonomous Agents Project 2024
#       Nikolaos Papoutsakis
#           2019030206

#  Project: Self-Driving RaceCar - AI using Pygame & NEAT (neural networks)

import pygame
import sys
import neat

from car import RaceCar
from utils import TRACK, SCREEN

# setup pygame env and run the sim
def setup_enviroment(genomes, config):
    global cars, ge, nets

    cars = []
    ge = []
    nets = []

    # we create a list of our car models and we feed the network with them
    for i, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(RaceCar()))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # draw the track on screen
        SCREEN.blit(TRACK, (0, 0))

        if len(cars) == 0:
            break

        for i, car in enumerate(cars):
            ge[i].fitness += 1

            # on each iteration we check if cars are alive, if not we remove them
            if not car.sprite.alive:
                cars.pop(i)
                ge.pop(i)
                nets.pop(i)

        #        Our desicion making
        #     sensor  ---->    output
        #       0
        #       1           steer_left  [0]
        #       2
        #       3           steer_right [1]
        #       4 
        # 
        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.getSensorData())
            if output[0] > 0.65:
                car.sprite.direction_vector = 1
            if output[1] > 0.65:
                car.sprite.direction_vector = -1
            if output[0] <= 0.65 and output[1] <= 0.65:
                car.sprite.direction_vector = 0

        
        # update display
        for car in cars:
            car.draw(SCREEN)
            car.update()
        pygame.display.update()
    return


#  Setup the neural network
#  https://neat-python.readthedocs.io/en/latest/xor_example.html#running-neat
def main(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))

    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.run(setup_enviroment, 30)
    return


# Run application
if __name__ == '__main__':
    main("config.txt")