'''
* @Author: csy 
* @Date: 2019-05-06 14:09:01 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-06 14:09:01 
'''
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
import pygame

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    # TODO:pylint检测pygame初始化不通过
    pygame.init()  # 初始化背景设置
    ai_settings = Settings()  # 加载Settings函数读取默认配置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))  # 根据Settings函数内定义的宽和高定义屏幕
    ship = Ship(ai_settings, screen)  # 加载Ship
    aliens = Group()  # 定义外星人组
    bullets = Group()  # 定义子弹组
    gf.create_fleet(ai_settings, screen, ship, aliens)  # 加载外星人群
    stats=GameStats(ai_settings)    #加载统计信息
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # 加载飞船事件
        if stats.game_active:
            ship.update()  # 调整飞船位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)  # 更新子弹
            gf.update_aliens(ai_settings, stats,screen,ship, aliens,bullets)  # 更新外星人状态
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 刷新屏幕


run_game()
