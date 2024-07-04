"""水花模块"""

import pygame
from pygame.sprite import Sprite

class Splash(Sprite):
    """水花类"""

    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)  # 创建一个透明的Surface
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.radius = 0  # 初始波纹半径
        self.max_radius = 30  # 波纹最大半径
        self.color = (0, 0, 255)  # 波纹颜色

    def update(self):
        """更新水花"""
        self.radius += 2  # 波纹半径增加的速度
        if self.radius > self.max_radius:
            self.kill()  # 当波纹扩散到最大半径时，删除水花对象

        # 绘制圆形波纹
        pygame.draw.circle(self.image, self.color, self.rect.center, self.radius)

        # 更新矩形位置，确保波纹在屏幕中心
        self.rect = self.image.get_rect(center=self.rect.center)