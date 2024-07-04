import sys
import pygame
from random import randint
from star import Star, CraftStar

class Main:

    def __init__(self) -> None:
        
        # 设置窗口大小
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.stars = pygame.sprite.Group()
        self.number = 30
        self.stars.add([ CraftStar(self) for _ in range(self.number) ])
        # self._create_star()
        # 设置标题
        pygame.display.set_caption("星星")


    def run_game(self):
        """开始游戏主循环"""
    
        while True:
            # 鼠标事件和键盘事件
            self._check_events()

            # 修改屏幕图像
            self._update_screen()

    def _create_star(self):
        """创建星星"""

        for number in range(self.number):
            random_number_x = randint(0, self.screen_width)
            random_number_y = randint(0, self.screen_height)
            star = Star(self)
            star.rect.x = random_number_x
            star.rect.y = random_number_y
            self.stars.add(star)

    def _check_events(self):
        """监视鼠标事件和键盘事件"""

        for event in pygame.event.get():
            # 检测到点击退出按钮
            if event.type == pygame.QUIT:
                sys.exit()

    
    def _update_screen(self):
        """更新屏幕图像,并使新屏幕可见"""

        # 重绘屏幕背景色
        self.screen.fill((230, 230, 230))

        self.stars.update()

        # self.stars.draw(self.screen)

        # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = Main()
    ai.run_game()