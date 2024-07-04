import sys
import pygame
from water import Water

class Main:

    def __init__(self) -> None:
        
        # 设置窗口大小
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.waters = pygame.sprite.Group()
        self.water_number = 50
        self.splashs = pygame.sprite.Group()
        self.waters.add([Water(self) for _ in range(self.water_number)])
        # 设置标题
        pygame.display.set_caption("水滴")
        # 创建时钟对象
        self.clock = pygame.time.Clock()


    def run_game(self):
        """开始游戏主循环"""
    
        while True:
            # 鼠标事件和键盘事件
            self._check_events()

            # self.splashs.update()
            self.waters.update()

            # 修改屏幕图像
            self._update_screen()

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

        self.waters.draw(self.screen)

        self.splashs.draw(self.screen)

        # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
        pygame.display.flip()

        # 设定帧率
        self.clock.tick(120)

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = Main()
    ai.run_game()