"""子弹模块"""

from typing import Any
import pygame
from pygame.sprite import Sprite
# from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 初始化一个 矩形资源
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 将值设置到飞机头部中间
        self.rect.midright = ai_game.ship.rect.midright

        # 存储子弹
        self.x = float(self.rect.x) 

    def update(self) -> None:
        """更新子弹的位置"""

        # 向上移动
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """绘制子弹"""

        pygame.draw.rect(self.screen, self.color, self.rect)
