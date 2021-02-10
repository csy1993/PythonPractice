'''
* @Author: csy 
* @Date: 2019-05-08 11:12:37 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-08 11:12:37 
'''
class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active=False

    def reset_stats(self):
        """初始化在线游戏期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
