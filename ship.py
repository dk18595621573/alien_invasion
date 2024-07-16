"""飞船模块"""

import pygame

class Ship:
    """飞船类"""

    def __init__(self, ai_game) -> None:
        """初始化飞船并设置飞船位置"""
        
        # 拿到屏幕的位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并外接矩形图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 放置飞船到底部中央(使用绘制的窗口比例大小)
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moveing_down = False

        self.settings = ai_game.settings

        # 存储小数值的飞船位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def center_ship(self):
        """居中飞船"""
        self.rect.midbottom = self.screen_rect.midbottom
        # 重新指定 x 坐标 y 坐标
        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动飞船"""

        # 移动标识为 true 并且 右边窗口像素>飞船移动像素
        if self.moving_right and self.screen_rect.right > self.rect.right:
            self.x += self.settings.ship_speed
        # 移动标识为 true 并且 左边窗口像素>飞船移动像素
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 移动标识为 true 并且 顶部窗口像素>飞船移动像素
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        # 移动标识为 true 并且 底部窗口像素>飞船移动像素
        if self.moveing_down and self.screen_rect.bottom > self.rect.bottom:
            self.y += self.settings.ship_speed

        # 更新实际飞船位置
        self.rect.x = self.x
        self.rect.y = self.y