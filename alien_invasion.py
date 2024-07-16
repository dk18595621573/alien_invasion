import sys
import pygame
import settings
import ship
import font
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏创建游戏资源"""

        pygame.init()
        self.settings = settings.Settings()
        # 设置窗口大小
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                        self.settings.screen_height))
        # 初始化飞船
        self.ship = ship.Ship(self)
        # 初始化字体
        self.font = font.Font(self)
        # 初始化子弹
        self.bullets = pygame.sprite.Group()
        # 初始化外星人
        self.aliens = pygame.sprite.Group()
        self._create_feet()
        # 设置标题
        pygame.display.set_caption("外星人入侵")
        # 创建时钟对象
        self.clock = pygame.time.Clock()
        self.stats = GameStats(self)

        self.text = ''

    def run_game(self):
        """开始游戏主循环"""
    
        while True:
            # 鼠标事件和键盘事件
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                # 更新子弹
                self._update_bullets()
                # 更新外星人位置
                self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """开火"""

        # 限制子弹数量
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(Bullet(self))
    
    def _update_bullets(self):
        """更新子弹"""

        self.bullets.update()
        # 超出屏幕 清空子弹
        for bullet in self.bullets.copy():
            if bullet.y < 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _create_feet(self):
        """创建外星人"""

        # 创建一组外星人
        alien = Alien(self)
        # 根据屏幕大小 间隔一个外星人绘制一个外星人
        alien_width = alien.rect.width
        alien_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = alien_space_x // (2 * alien_width)
        # 获取可以创建多少行外星人
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        alien_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_alien_y = alien_space_y // (2 * alien_height)
        # 创建外星人组
        for rows_number in range(number_alien_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(rows_number, alien_number)
    
    def _create_alien(self, rows_number, alien_number):
        """创建一个外星人并放到当前行"""
        alien = Alien(self)
        # 绘制外星人
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # 绘制行数
        alien.rect.y = alien_height + 2 * alien_height * rows_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """更新外星人位置"""

        self._check_fleet_edges()
        self.aliens.update()
        #检查外星人是否和飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """响应外星人和飞船碰撞事件"""

        if self.stats.bullet_left > 0:

            # 飞船数量减少
            self.stats.bullet_left -= 1
            # 清空外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群外星人 并将飞船居中
            self._create_feet()
            self.ship.center_ship()

            sleep(1)
        else:
            self.stats.game_active = False

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""

        # 检测是否有外星人被子弹击中
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)

        # 判断外星人是否被全部消灭
        if not self.aliens:
            # 清空子弹创建外星人
            self.bullets.empty()
            self._create_feet()

    def _check_fleet_edges(self):
        """检测到碰到墙壁做出处理"""

        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """控制移动方向遇到墙壁向下移动"""
        
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        # 将正设置成负 将负设计成正
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕图像,并使新屏幕可见"""

        # 重绘屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 让飞船显示在屏幕上
        self.ship.blitme()

        # 让子弹显示在屏幕上
        for bullet in self.bullets:
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # 让文字显示在屏幕上
        # self.font.blitme(self.text)

        # 刷新屏幕可见(擦去旧屏幕 使新屏幕可见)
        pygame.display.flip()

        # 设定帧率
        self.clock.tick(90)

if __name__ == '__main__':
    # 创建游戏并且运行
    ai = AlienInvasion()
    ai.run_game()