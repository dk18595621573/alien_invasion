"""外星人模块"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人类"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        # 拿到屏幕的位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储精准位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

