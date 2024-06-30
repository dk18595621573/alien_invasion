"""星星模块"""

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """星星类"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        # 拿到屏幕的位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/star.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储精准位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

