import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position"""
		super().__init__()
		self.screen= screen
		self.ai_settings= ai_settings
		
		#Load the alien image and set its rect attribute
		self.image= pygame.image.load('images/alien.bmp')
		self.rect= self.image.get_rect()
		self.width= self.rect.width
		self.height= self.rect.height
		
		#set starting position near the top left of the screen
		self.rect.x= self.width
		self.rect.y= self.height
		
		self.x= float(self.rect.x)
		self.y= float(self.rect.y)
	
	def check_edges(self):
		"""Return true if alien is at the edge"""
		screen_rect= self.screen.get_rect()
		if (self.rect.right >= screen_rect.right - 20) or self.rect.left <= 20:
			return True
		
	def update(self):
		"""Move the alien position over time"""
		speed = self.ai_settings.alien_speed
		xdirection = self.ai_settings.fleet_xdirection
		self.x += (speed * xdirection)
		self.rect.x= self.x
			 
	def blitme(self):
		"""Draw alien at its current location"""
		self.screen.blit(self.image, self.rect)
