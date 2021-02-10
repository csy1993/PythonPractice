'''
* @Author: csy 
* @Date: 2019-05-06 14:09:08 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-06 14:09:08 
'''


class Settings():
    """存储游戏设置的类"""

    def __init__(self):
        '''初始化设置'''
        self.screen_width = 1200  # 定义屏幕宽
        self.screen_height = 800  # 定义屏幕高
        self.bg_color = (230, 230, 230)  # 定义背景色
        
        self.ship_speed_factor = 2  # 定义飞船速度
        self.ship_limit=3  #定义飞船数


        self.bullet_speed_factor = 5  # 定义子弹速度
        self.bullet_width = 3  # 定义子弹宽
        self.bullet_height = 15  # 定义子弹高
        self.bullet_color = (255, 0, 0)  # 定义子弹色
        self.bullets_allowed = 100  # 定义子弹数

        self.alien_speed_factor = 1  # 定义外星人速度
        self.fleet_drop_speed = 50  # 定义外星人下落速度
        self.fleet_direction = 1  # 定义外星人方向

