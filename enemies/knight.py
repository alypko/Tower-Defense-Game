import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/10", "10_enemies_1_run_0" + add_str + ".png")).convert_alpha(),
        (100, 100)))


class Knight(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "knight"
        self.money = 100
        self.imgs = imgs[:]
        self.max_health = 50
        self.health = self.max_health
