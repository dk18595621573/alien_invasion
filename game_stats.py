"""游戏统计模块"""

class GameStats:
    """游戏统计类"""

    def __init__(self, ai_game) -> None:

        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化统计信息"""

        self.bullet_left = self.settings.ship_limit
        self.game_active = True