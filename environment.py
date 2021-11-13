import pygame
import os


class Environment:
    pygame.init()

    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 1100

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    BACKGROUND = pygame.image.load(os.path.join("assets/images", "track.png"))

    FONT = pygame.font.Font(pygame.font.get_default_font(), 20)

    LARGE_CACTUS = [
        pygame.image.load(os.path.join("assets/cactus", "large-cactus-1.png")),
        pygame.image.load(os.path.join("assets/cactus", "large-cactus-2.png")),
        pygame.image.load(os.path.join("assets/cactus", "large-cactus-3.png")),
    ]

    SMALL_CACTUS = [
        pygame.image.load(os.path.join("assets/cactus", "small-cactus-1.png")),
        pygame.image.load(os.path.join("assets/cactus", "small-cactus-2.png")),
        pygame.image.load(os.path.join("assets/cactus", "small-cactus-3.png")),
    ]
