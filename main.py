import os
import sys
import math
import neat
import pygame
import random
from dinosaur import Dinosaur
from environment import Environment
from large_cactus import LargeCactus
from small_cactus import SmallCactus


def Get_Distance(nr_Position_A, nr_Position_B):
    nr_Distance_X = nr_Position_A[0] - nr_Position_B[0]
    nr_Distance_Y = nr_Position_A[1] - nr_Position_B[1]
    return math.sqrt(nr_Distance_X ** 2 + nr_Distance_Y ** 2)


def Get_Genomes(genomes, config):
    global nr_Game_Speed, nr_X_Position_Background, nr_Y_Position_Background, obstacles, dinosaurs, nr_Points, ge, networks

    nr_Points = 0
    clock = pygame.time.Clock()

    obstacles = []
    dinosaurs = []
    ge = []
    networks = []

    nr_X_Position_Background = 0
    nr_Y_Position_Background = 380
    nr_Game_Speed = 20

    for cd_Genome, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        genome.fitness = 0

    def Set_Score():
        global nr_Points, nr_Game_Speed
        nr_Points += 1
        if nr_Points % 100 == 0:
            nr_Game_Speed += 1
        text = Environment.FONT.render(f'Points: {str(nr_Points)}', True, (0, 0, 0))
        Environment.SCREEN.blit(text, (950, 50))

    def Set_Background():
        global nr_X_Position_Background, nr_Y_Position_Background
        nr_Image_Width = Environment.BACKGROUND.get_width()
        Environment.SCREEN.blit(Environment.BACKGROUND, (nr_X_Position_Background, nr_Y_Position_Background))
        Environment.SCREEN.blit(Environment.BACKGROUND,
                                (nr_X_Position_Background + nr_Image_Width, nr_Y_Position_Background))

        if nr_X_Position_Background < -nr_Image_Width:
            nr_X_Position_Background = 0

        nr_X_Position_Background -= nr_Game_Speed

    b_Running = True

    while b_Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Environment.SCREEN.fill((255, 255, 255))

        for dinosaur in dinosaurs:
            dinosaur.Update()
            dinosaur.Draw(Environment.SCREEN)

        if len(dinosaurs) == 0:
            break

        if len(obstacles) == 0:
            nr_Random_Int = random.randint(0, 1)

            if nr_Random_Int == 0:
                obstacles.append(SmallCactus(Environment.SMALL_CACTUS, random.randint(0, 2)))
            elif nr_Random_Int == 1:
                obstacles.append(LargeCactus(Environment.LARGE_CACTUS, random.randint(0, 2)))

        for obstacle in obstacles:
            obstacle.Draw()
            obstacle.Update(nr_Game_Speed, obstacles)

            for i, dinosaur in enumerate(dinosaurs):
                if dinosaur.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1
                    ge.pop(i)
                    networks.pop(i)
                    dinosaurs.pop(i)

            for i, dinosaur in enumerate(dinosaurs):
                output = networks[i].activate((dinosaur.rect.y,
                                               Get_Distance((dinosaur.rect.x, dinosaur.rect.y), obstacle.rect.midtop)))

                if output[0] > 0.5 and dinosaur.rect.y == dinosaur.NR_Y_POSITION:
                    dinosaur.b_Dinosaur_Jumping = True
                    dinosaur.b_Dinosaur_Running = False

        Set_Score()
        Set_Background()
        clock.tick(30)
        pygame.display.update()


def Run(ds_Config_Path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        ds_Config_Path
    )
    population = neat.Population(config)
    population.run(Get_Genomes, 50)


if __name__ == '__main__':
    ds_Local_Dir = os.path.dirname(__file__)
    ds_Config_Path = os.path.join(ds_Local_Dir, 'config.txt')
    Run(ds_Config_Path)
