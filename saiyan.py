"""赛亚人模块"""

import pygame
from alien_invasion import AlienInvasion

class Saiyan:
    """赛亚人类"""

    def __init__(self, ai_game: AlienInvasion) -> None:
        """初始化相关配置"""

        self.screen = ai_game.screen
        # 拿到屏幕矩形
        self.screen_rect = ai_game.screen.get_rect()
        # 加载图像
        self.image = pygame.image.load('images/syr.bmp')
        self.image = pygame.transform.scale(self.image, (288, 320))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)