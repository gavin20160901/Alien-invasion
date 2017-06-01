#coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien


#重构代码
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		#按下右键飞船右移
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		#按下右键飞船右移
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	#响应按键和鼠标
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
	#创建一颗子弹并加入到bullets中,最多屏幕上同时显示5颗子弹
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullte = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullte)

def update_bullets(bullets):
	bullets.update()
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))

def get_number_aliens_x(ai_settings, alien_width):
	#先创建一个外星人,计算一行可以容纳的数量
	#外星人之间间距为一个外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_bunber):
    """创建一行外星人.并加入当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_bunber
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	#创建外星人群
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, 
    	alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

'''
def create_fleet(ai_settings, screen, aliens):
	#创建外星人群
	#先创建一个外星人,计算一行可以容纳的数量
	#外星人之间间距为一个外星人宽度
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_spcae_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_spcae_x / (2 * alien_width))

	#创建一行外星人
	for alien_number in range(number_aliens_x):
		#创建外星人并加入当前行
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)
'''

def update_aliens(aliens):
	"""更新外星人位置"""
	aliens.update()

def update_screen(ai_settings, screen, ship, aliens, bullets):
	#更新屏幕上的图像,并切换到新屏幕
	#每次循环都要重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#alien.blitme()
	aliens.draw(screen)

	pygame.display.flip()