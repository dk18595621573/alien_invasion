"""星星模块"""

from typing import Any
import pygame
import math
import random
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


class CraftStar(Sprite):
    """手工绘制星星类"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.x = random.randint(0, ai_game.screen_width)
        self.y = random.randint(0, ai_game.screen_height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        

    def _generate_star_points(self, center_x, center_y, outer_radius, inner_radius):
        """定义五角星的顶点坐标"""
        
        points = []
        angle = - math.pi / 2
        for i in range(5):
            outer_x = center_x + outer_radius * math.cos(angle + i * 2 * math.pi / 5)
            outer_y = center_y + outer_radius * math.sin(angle + i * 2 * math.pi / 5)
            points.append((outer_x, outer_y))
            inner_x = center_x + inner_radius * math.cos(angle + (i + 0.5) * 2 * math.pi / 5)
            inner_y = center_y + inner_radius * math.sin(angle + (i + 0.5) * 2 * math.pi / 5)
            points.append((inner_x, inner_y))
        return points
    
    def update(self) -> None:
        
        star_points = self._generate_star_points(self.x, self.y, 20, 8)
        pygame.draw.polygon(self.screen, self.color, star_points)