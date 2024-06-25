import sys
import pygame
import settings
import ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏创建游戏资源"""

        pygame.init()
        self.settings = settings.Settings()
        # 设置窗口大小
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                        self.settings.screen_height))
        # 设置标题
        pygame.display.set_caption("外星人入侵")
        # 初始化飞船
        self.ship = ship.Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 鼠标事件和键盘事件
            self._check_events()
            # 修改屏幕图像
            self._update_screen()

    def _check_events(self):
        """监视鼠标事件和键盘事件"""

        for event in pygame.event.get():
                # 检测到点击退出按钮
                if event.type == pygame.QUIT:
                    print("退出成功...")
                    sys.exit()
    
    def _update_screen(self):
        """更新屏幕图像,并使新屏幕可见"""

        # 重绘屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 让飞船显示在屏幕上
        self.ship.blitme()
        # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = AlienInvasion()
    ai.run_game()