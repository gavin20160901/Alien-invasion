#coding=utf-8
import sys
import pygame
from bullet import Bullet


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

def update_screen(ai_settings, screen, ship, bullets):
	#更新屏幕上的图像,并切换到新屏幕
	#每次循环都要重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	pygame.display.flip()