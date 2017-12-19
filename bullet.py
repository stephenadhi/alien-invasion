import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A Class to manage bullets fired from the ship"""
	
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen= screen
		self.color= ai_settings.bullet_color
		self.speed= ai_settings.bullet_speed
		
		#Create bullet rect and set position
		self.rect= pygame.Rect(0, 0, ai_settings.bullet_width, 
			ai_settings.bullet_height)
		self.rect.centerx= ship.rect.centerx
		self.rect.top= ship.rect.top
		
		#Store bullet y-position as float
		self.y= float(self.rect.y)
		
	def update(self):
		"""Move the bullet up the screen."""
		self.y -= self.speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
