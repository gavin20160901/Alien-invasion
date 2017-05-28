#coding=utf-8

class Settings():
	#存储所有设置
	
	#初始化游戏设置
	def __init__(self):
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#飞船速度设置
		self.ship_speed_factor = 1.5

		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		#屏幕上的子弹数量限制
		self.bullets_allowed = 5