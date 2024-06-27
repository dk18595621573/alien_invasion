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
        self.ship_speed = 1.5
        # 创建一个字体对象
        self.font_model = 'Arial'
        self.font_size = 24
        self.font_black = (0, 0, 0)