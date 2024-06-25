"""飞船模块"""

import pygame
from alien_invasion import AlienInvasion

class Ship:
    """飞船类"""

    def __init__(self, ai_game: AlienInvasion) -> None:
        """初始化飞船并设置飞船位置"""
        
        # 拿到屏幕的位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并外接矩形图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 放置飞船到底部中央(使用绘制的窗口比例大小)
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
