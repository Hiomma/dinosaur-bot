from environment import Environment

class Obstacle:
    def __init__(self, image, nr_Cacti):
        self.image = image
        self.nr_Cacti = nr_Cacti
        self.rect = self.image[nr_Cacti].get_rect()
        self.rect.x = Environment.SCREEN_WIDTH

    def Update(self, nr_Game_Speed,obstacles):
        self.rect.x -= nr_Game_Speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def Draw(self):
        Environment.SCREEN.blit(self.image[self.nr_Cacti], self.rect)

