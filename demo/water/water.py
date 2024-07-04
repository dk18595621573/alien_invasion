"""水滴模块"""

import pygame
from pygame.sprite import Sprite
from random import randint
from demo.water.splash import Splash

class Water(Sprite):
    """水滴类"""

    def __init__(self, w_main):
        super().__init__()
        self.splashs = w_main.splashs
        # 拿到屏幕的位置
        self.screen_width = w_main.screen_width
        self.screen_height = w_main.screen_height
        self.image = pygame.image.load('images/water.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_width)
        self.rect.top = 0
        self.speed = self._speed_init()

    def update(self):
        """移动水滴"""
        
        # 向下移动
        self.rect.y += self.speed

        # 如果水滴移出屏幕底部，则重新放置到屏幕顶部
        if self.rect.top > self.screen_height:
            self.rect.top = 0
            self.speed = self._speed_init()
            # splash = Splash(self.rect.center)
            # self.splashs.add(splash)
            

    def _speed_init(self) -> int:
        """移动速度"""

        return randint(3, 10)

