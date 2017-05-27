import pygame

from ai_settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船
	ship = Ship(ai_settings, screen)

	#开始游戏的主循环
	while  True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#每次循环时都重绘屏幕
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		#让新绘制的屏幕可见
		pygame.display.flip()

run_game()