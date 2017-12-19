import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien
from ship import Ship

def check_events(ai_settings, screen, ship, aliens, play_button, 
stats, bullets, scoreboard):
	"""Respond to kepresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, stats, ship, 
			screen, aliens, bullets, scoreboard)		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,
			 ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y= pygame.mouse.get_pos()
			check_play_click(ai_settings, screen, ship, aliens, 
			play_button, stats, bullets, scoreboard, mouse_x, mouse_y)	 		

def check_keydown_events(event, ai_settings, stats, ship, screen, 
aliens, bullets, scoreboard):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_p:
		startgame(ai_settings, stats, aliens, bullets, screen, 
		ship, scoreboard)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_play_click(ai_settings, screen, ship, aliens, 
play_button, stats, bullets, scoreboard, mouse_x, mouse_y):
	play_clicked= play_button.rect.collidepoint(mouse_x, mouse_y)
	if play_clicked and not stats.game_active:
		startgame(ai_settings, stats, aliens, bullets, screen, 
		ship, scoreboard)
		
def startgame(ai_settings, stats, aliens, bullets, screen, ship, 
scoreboard):
	stats.game_active= True
	pygame.mouse.set_visible(False)
	#Reset game settings
	ai_settings.initialize_dynamic_settings()
	stats.reset_stats()
	scoreboard.prep_score()
	scoreboard.prep_ships()
	scoreboard.show_score()
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()

def check_keyup_events(event, ship): 						
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_UP:
		ship.moving_up = False
	if event.key == pygame.K_DOWN:
		ship.moving_down = False
		
		
def get_number_aliens_x(ai_settings, alien_width):
	"""Determine the number of aliens in a row"""
	available_space_x= ai_settings.screen_width - 2 * alien_width  
	number_aliens_x= int(available_space_x / (2.5 * alien_width))
	return number_aliens_x
	
	
def get_number_rows(ai_settings, ship_height, alien_height):
	"""Determine the number of alien rows"""
	available_row= ai_settings.screen_height - 3*alien_height - ship_height 
	number_rows= int(available_row / (3 * alien_height))
	return number_rows
	
	
def create_alien(ai_settings, screen, aliens, alien_number, n_row):
	"""Create an alien and place it in the row"""
	alien= Alien(ai_settings, screen)
	alien_width= alien.width
	alien_height= alien.height
	alien.x = alien.width + (2 * alien_width * alien_number)
	alien.y = 1.5 * alien_height + 1.5 * alien_height * n_row
	alien.rect.x= alien.x
	alien.rect.y= alien.y
	aliens.add(alien)
	
		
def create_fleet(ai_settings, screen, ship, aliens):
	"""Create a full fleet of aliens"""
	alien= Alien(ai_settings, screen)
	number_aliens_x= get_number_aliens_x(ai_settings, alien.width)
	number_rows= get_number_rows(ai_settings, ship.height, alien.height) 
	for n_row in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, n_row)

def check_fleet_edges(aliens, ai_settings):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens, ai_settings)
			break

def change_fleet_direction(aliens, ai_settings):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_xdirection *= -1


def fire_bullets(ai_settings, screen, ship, bullets):
	#Create new bullet and add it to the group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet= Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

	
def update_bullets(bullets, aliens, ai_settings, stats,
screen, scoreboard, ship):
	bullets.update()
	#Get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collision(bullets, aliens, ai_settings, 
	stats, screen, scoreboard, ship)

def ship_hit(ai_settings, stats, screen, ship, aliens, 
bullets, scoreboard):
	"""Respond to ship being hit by alien"""
	if stats.ships_left > 0:
		stats.ships_left -= 1
		#pause
		sleep(0.5)
		#Reset aliens, bullets, fleet, ship
		aliens.empty()
		bullets.empty()
		ship.center_ship()
		for ship in scoreboard.ships.copy():
			scoreboard.ships.remove(ship)
		scoreboard.prep_ships()
		create_fleet(ai_settings, screen, ship, aliens)
		
	else:
		stats.game_active= False
		pygame.mouse.set_visible(True)
	
def check_bullet_alien_collision(bullets, aliens, ai_settings, 
stats, screen, scoreboard, ship):	
	#Check collision
	collision= pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collision:
		for aliens in collision.values():
			stats.score += ai_settings.alien_points * len(aliens)
			scoreboard.prep_score()
	check_highscore(stats, scoreboard)
	#Check whether to create new fleet, if true increase speed
	if len(aliens)==0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)
	
def check_highscore(stats, scoreboard):
	if stats.score > stats.highscore:
		stats.highscore= stats.score
		scoreboard.prep_highscore()

def check_aliens_bottom(ai_settings, stats, screen, ship, 
aliens, bullets, scoreboard):
	screen_rect = screen.get_rect() 
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, 
			bullets, scoreboard)
			break

def update_aliens(ai_settings, stats, screen, ship, aliens, 
bullets, scoreboard):
	"""update the position of all aliens"""
	check_fleet_edges(aliens, ai_settings)
	aliens.update()
	#Look for alien-ship collision
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, 
		bullets, scoreboard)
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, 
	bullets, scoreboard)
		
def update_screen(ai_settings, screen, stats, scoreboard, 
ship, aliens, bullets, play_button):		
	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#Draw play button if game is inactive
	if not stats.game_active:
		play_button.draw_button()
	#Display scoreboard
	scoreboard.show_score()
	
	pygame.display.flip()
