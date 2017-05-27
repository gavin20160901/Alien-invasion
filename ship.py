import pygame

#创建ship类
class Ship():
	"""初始化飞船"""
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放到底部中间
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#在飞船属性center中存浮点数值
		self.center = float(self.rect.centerx)
		
		#飞船移动状态标识
		self.moving_right = False
		self.moving_left = False

	def update(self):
		#根据移动标识调整飞船位置,并限制移动范围不能超过屏幕范围
		if self.moving_right  and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		#根据center更新rect对象
		self.rect.centerx = self.center

	def blitme(self):
		#指定位置绘制飞船
		self.screen.blit(self.image, self.rect)
