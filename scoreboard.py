import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""A class to report scoring information"""
	
	def __init__(self, ai_settings, screen, stats, ship):
		"""Initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats= stats
		self.ship= ship
		self.ships= Group()
		
		#Font settings
		self.text_color= (30, 30, 30)
		self.font= pygame.font.SysFont(None, 48)
		
		self.prep_ships()
		self.prep_score()
		self.prep_highscore()
	
	def prep_ships(self):
		"""Show how many ships are left"""
		for ship_number in range(self.stats.ships_left):
			ship= Ship(self.ai_settings, self.screen)
			ship.rect.x= 10 + ship_number * ship.rect2.width
			ship.rect.y= 10
			self.ships.add(ship)
			
	def prep_score(self):
		"""Turn the score into rendered image"""
		rounded_score= round(self.stats.score, -1)
		self.score_str= "{:,}".format(rounded_score)
		self.score_image= self.font.render(self.score_str, True, 
		self.text_color, self.ai_settings.bg_color)
		#Display score 
		self.score_rect= self.score_image.get_rect()
		self.score_rect.right= self.screen_rect.right - 20
		self.score_rect.top= 10
	
	def prep_highscore(self):
		rounded_highscore= round(self.stats.highscore, -1)
		self.highscore_str= "{:,}".format(rounded_highscore)
		self.highscore_image= self.font.render(self.score_str, True, 
		self.text_color, self.ai_settings.bg_color)
		#Display score 
		self.highscore_rect= self.score_image.get_rect()
		self.highscore_rect.centerx= self.screen_rect.centerx
		self.highscore_rect.top= 10
		
	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.highscore_image, self.highscore_rect)
		self.ships.draw(self.screen)
