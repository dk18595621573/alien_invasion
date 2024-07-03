"""外星人模块"""

from typing import Any
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
        # self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.settings = ai_game.settings

        # 存储精准位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """外星人移动"""

        self.x = (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x += float(self.x)

    def check_edges(self):
        """校验是否到达屏幕边缘"""

        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True
        
    
