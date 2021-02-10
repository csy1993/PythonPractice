'''
* @Author: csy 
* @Date: 2019-05-06 16:48:23 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-06 16:48:23 
'''
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def get_number_aliens_x(ai_settings, alien_width):
    '''计算每行可容纳的外星人'''
    available_space_x = ai_settings.screen_width - \
        2 * alien_width  # 屏幕宽去掉2个外星人宽，为实际可用宽
    # 为每个外星人的右边空出一个外星人宽度，可得最多外星人数
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_height)  # 屏幕高度去掉飞船和3个外星人高度，为实际可用高
    number_rows = int(available_space_y /
                      (2 * alien_height))  # 为每个外星人的下边空出一个外星人高度，可得最多外星人行数
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人到当前行'''
    alien = Alien(ai_settings, screen)  # 调用类Alien
    alien_width = alien.rect.width  # 定义外星人宽
    alien.x = alien_width + 2 * alien_width * alien_number  # 根据外星人数获取外星人横坐标
    alien.rect.y = alien.rect.height + 2 * \
        alien.rect.height * row_number  # 根据外星人数获取外星人纵坐标
    alien.rect.x = alien.x
    aliens.add(alien)  # 将外星人放入外星人群


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings, screen)  # 实例化外星人类
    number_aliens_x = get_number_aliens_x(
        ai_settings, alien.rect.width)  # 获取一行外星人数
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)  # 获取可容纳行数
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit("Goodbye")
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键'''
    if event.key == pygame.K_q:
        exit("Goodbye")
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_fleet_edges(ai_settings, aliens):
    '''有外星人到达边缘后处理'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    '''响应子弹和外星人的碰撞'''
    collisions = pygame.sprite.groupcollide(
        bullets, aliens, True, True)  # 该函数遍历子弹和外星人，当重叠时，两个true参数会删除子弹和外星人
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检测外星人是否到底"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def change_fleet_direction(ai_settings, aliens):
    '''使整体外星人下降和改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed  # 使外星人下降
    ai_settings.fleet_direction *= -1  # 切換外星人群方向


def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    screen.fill(ai_settings.bg_color)  # 填充屏幕颜色
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # 画出飞船
    aliens.draw(screen)  # 画出外星人
    pygame.display.flip()  # 让最近绘制的屏幕可见


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''更新子弹位置和删除已消失子弹'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''检查外星人是否出界并更新位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    '''如果没有到达限制就发射一颗子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1  # 飞船数减1
        aliens.empty()
        bullets.empty()
    else:
        stats.game_active = False

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(0.5)
