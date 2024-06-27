import sys
import pygame
import settings
import ship
import font

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

        self.text = ''

    def run_game(self):
        """开始游戏主循环"""
        # 初始化飞船
        self.ship = ship.Ship(self)
        # 初始化字体
        self.font = font.Font(self, self.settings.font_model, self.settings.font_size)
        while True:
            # 鼠标事件和键盘事件
            self._check_events()
            self.ship.update()
            # 修改屏幕图像
            self._update_screen()

    def _check_events(self):
        """监视鼠标事件和键盘事件"""

        for event in pygame.event.get():
            # 检测到点击退出按钮
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_up_events(self, event):
        """抬起事件"""
       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            # 按下上移动按钮
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # 按下下移动按钮
            self.ship.moveing_down = False
    
    def _check_down_events(self, event):
        """键盘事件"""

        self.text = event.key
        if event.key == pygame.K_RIGHT:
            # 按下右移动按钮
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 按下左移动按钮
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # 按下上移动按钮
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # 按下下移动按钮
            self.ship.moveing_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _update_screen(self):
        """更新屏幕图像,并使新屏幕可见"""

        # 重绘屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 让飞船显示在屏幕上
        self.ship.blitme()

        # 让文字显示在屏幕上
        self.font.blitme(self.text)

        # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = AlienInvasion()
    ai.run_game()