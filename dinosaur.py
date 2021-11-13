import pygame
import os

class Dinosaur:
    NR_X_POSITION = 80
    NR_Y_POSITION = 310
    NR_JUMP_VELOCITY = 8.5

    RUNNING = [
        pygame.image.load(os.path.join("assets/dino", "dino-running-1.png")),
        pygame.image.load(os.path.join("assets/dino", "dino-running-2.png"))
    ]

    JUMPING = pygame.image.load(os.path.join("assets/dino", "dino-jumping.png"))

    def __init__(self, image=RUNNING[0]):
        self.image = image
        self.b_Dinosaur_Running = True
        self.b_Dinosaur_Jumping = False
        self.nr_Jump_Velocity = self.NR_JUMP_VELOCITY
        self.rect = pygame.Rect(self.NR_X_POSITION, self.NR_Y_POSITION, self.image.get_width(), self.image.get_height())
        self.nr_Step_Index = 0

    def Update(self):
        if self.b_Dinosaur_Running:
            self.Run()
        elif self.b_Dinosaur_Jumping:
            self.Jump()

        if self.nr_Step_Index >= 10:
            self.nr_Step_Index = 0

    def Jump(self):
        self.image = self.JUMPING
        if self.b_Dinosaur_Jumping:
            self.rect.y -= self.nr_Jump_Velocity * 4
            self.nr_Jump_Velocity -= 0.8
        if self.nr_Jump_Velocity <= -self.NR_JUMP_VELOCITY:
            self.b_Dinosaur_Jumping = False
            self.b_Dinosaur_Running = True
            self.nr_Jump_Velocity = self.NR_JUMP_VELOCITY

    def Run(self):
        self.image = self.RUNNING[self.nr_Step_Index // 5]
        self.rect.x = self.NR_X_POSITION
        self.rect.y = self.NR_Y_POSITION
        self.nr_Step_Index += 1

    def Draw(self, screen):
        screen.blit(self.image, self.rect)
