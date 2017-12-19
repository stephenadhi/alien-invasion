import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and its starting position"""
		super().__init__()
		self.screen= screen
		self.ai_settings= ai_settings
		
		#Load the ship image and get its rect.
		self.image1= pygame.image.load('images/ship.bmp')
		self.image= pygame.image.load('images/shiplives.bmp')
		self.rect= self.image1.get_rect()
		self.rect2= self.image.get_rect()
		self.width= self.rect.width
		self.height= self.rect.height
		self.screen_rect= screen.get_rect()
		
		#Start each new ship at the bottom of the screen
		self.rect.centerx= self.screen_rect.centerx
		self.center= float(self.rect.centerx)
		self.rect.bottom= self.screen_rect.bottom  
		self.bottom= float(self.rect.bottom)
		
		#Movement Flag
		self.moving_right = False               
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		
	def update(self):  
		"""Move ship during keydown_events""" 
		if self.moving_right:
			if (self.center + 60) < self.screen_rect.right:
				self.center += self.ai_settings.ship_speed
				
		elif self.moving_left:
			if (self.center - 60) > self.screen_rect.left:
				self.center -= self.ai_settings.ship_speed
		
		elif self.moving_up:
			if (self.bottom - 150) > self.screen_rect.top:
				self.bottom -= self.ai_settings.ship_speed
		
		elif self.moving_down:
			if self.bottom < self.screen_rect.bottom:
				self.bottom += self.ai_settings.ship_speed
			
		self.rect.centerx= self.center
		self.rect.bottom= self.bottom
		
	def center_ship(self):
		"""Center the ship on the screen"""
		self.center= self.screen_rect.centerx
		self.bottom= self.screen_rect.bottom
		
	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image1, self.rect)
	
	def draw_shiplives(self):
		self.screen.blit(self.image, self.rect2)
