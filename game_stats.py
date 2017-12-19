class GameStats():
	"""A class that tracks several game statistics"""
	
	def __init__(self, ai_settings):
		self.game_active= False
		"""Initialize stats"""
		self.ai_settings= ai_settings
		self.ships_left= self.ai_settings.ship_limit
		self.score= 0
		#Highscore should never be reset
		self.highscore= 0
		
	def reset_stats(self):
		self.ships_left= self.ai_settings.ship_limit
		self.score= 0
		
	
	
