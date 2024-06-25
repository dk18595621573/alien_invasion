import sys
import pygame
from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏创建游戏资源"""

        pygame.init()
        self.settings = Settings()
        # 设置窗口大小
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                        self.settings.screen_height))
        # 设置标题
        pygame.display.set_caption("外星人入侵")

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视鼠标事件和键盘事件
            for event in pygame.event.get():
                # 检测到点击退出按钮
                if event.type == pygame.QUIT:
                    print("退出成功...")
                    sys.exit()
                # 重绘屏幕背景色
                self.screen.fill(self.settings.bg_color)
                # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
                pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = AlienInvasion()
    ai.run_game()