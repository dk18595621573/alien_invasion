"""字体模块"""

import pygame

class Font:
    """字体类"""
    
    def __init__(self, ai_game) -> None:
        """初始化"""

        self.settings = ai_game.settings

        # 拿取屏幕位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 初始化字体模块
        pygame.font.init()
        # 创建一个字体对象
        self.sys_font = pygame.font.SysFont(self.settings.font_model, self.settings.font_size)

    def blitme(self, text):
        """绘制渲染文字"""

        text_surface = self.sys_font.render(f"{text}", True, self.settings.font_black)
        text_rect = text_surface.get_rect()
        # 将文字表面放置在屏幕顶部
        text_rect.top = self.screen_rect.top
        # 绘制文字表面到屏幕
        self.screen.blit(text_surface, text_rect)
