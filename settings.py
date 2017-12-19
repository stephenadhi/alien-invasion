class Settings():
	"""A class to store all settings for Alien Invasion"""
	
	def __init__(self):
		#Screen settings
		self.screen_width=1200
		self.screen_height=700
		self.bg_color = (230,230,230)    
		
		#Ship settings    
		self.ship_limit = 3           

		#Bullet settings
		self.bullet_width = 3
		self.bullet_height = 12
		self.bullet_color = (60,60,60)
		self.bullets_allowed= 5
		
		#Alien settings
		self.fleet_drop_speed = 15
		
		#Game speed settings
		self.speedup_scale= 1.1
		self.initialize_dynamic_settings()
		
		#Scoring
		self.alien_points= 50
		self.score_scale= 1.3
		
	def initialize_dynamic_settings(self):
		self.ship_speed = 2.5
		self.bullet_speed = 1.5
		self.alien_speed = 1.5
		self.fleet_xdirection = 1
		
	def increase_speed(self):
		self.ship_speed *= (0.8*self.speedup_scale)
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points*self.score_scale)
		
	
