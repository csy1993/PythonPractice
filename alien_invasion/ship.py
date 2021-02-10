'''
* @Author: csy 
* @Date: 2019-05-06 14:09:16 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-06 14:09:16 
'''
import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置初始化位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')  # 加载飞船图片
        self.rect = self.image.get_rect()  # 定义飞船矩形区域
        self.screen_rect = screen.get_rect()  # 定义屏幕矩形区域
        self.rect.centerx = self.screen_rect.centerx  # 将屏幕X轴中心赋值给飞船
        self.rect.bottom = self.screen_rect.bottom  # 将屏幕底部赋值给飞船
        self.center = float(self.rect.centerx)  # 在飞船的属性center中存储小数值
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center  # 根据self.center更新rect
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center=self.screen_rect.centerx