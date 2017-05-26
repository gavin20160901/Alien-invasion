import pygame

#创建ship类
class Ship():
	"""初始化飞船"""
	def __init__(self, screen):
		self.screen = screen
		#加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放到底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		#指定位置绘制飞船
		self.screen.blit(self.image, self.rect)
