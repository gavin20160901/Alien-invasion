
import sys

import pygame

def check_events(ship):
	#响应按键和鼠标
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				#按下右键飞船右移
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				#松开右键飞船停止
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False


def update_screen(ai_settings, screen, ship):
	#更新屏幕上的图像,并切换到新屏幕
	#每次循环都要重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	pygame.display.flip()