from obstacle import Obstacle

class LargeCactus(Obstacle):
    def __init__(self, image, nr_Cacti):
        super().__init__(image, nr_Cacti)
        self.rect.y = 300