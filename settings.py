"""设置模块"""

class Settings:
    """存储一些设置信息"""

    def __init__(self) -> None:
        # 窗口大小
        self.screen_width = 1200
        self.screen_height = 800
        # 颜色
        self.bg_color = (230, 230, 230)
        # 飞船移动速度
        self.ship_speed = 3
        # 创建一个字体对象
        self.font_model = 'Arial'
        self.font_size = 24
        self.font_black = (0, 0, 0)

        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 400
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 1
        # 1表示向右移动 -1 表示向左移动
        self.fleet_direction = 1
        # 向下移动间隔
        self.fleet_drop_speed = 1

        # 星星的数量
        self.star_number = 20