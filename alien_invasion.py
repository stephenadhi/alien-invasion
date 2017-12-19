#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#  
#  Copyright 2017 Stephen Adhi <superuser@superuser-X450CP>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Project idea based on the "Python Crash Course" book by Eric Matthes.

import sys

import pygame 
from pygame.sprite import Group

from play_button import PlayButton
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf


def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings= Settings()
	screen= pygame.display.set_mode((ai_settings.screen_width, 
	    ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#Make play button
	play_button= PlayButton(ai_settings, screen, "Play") 
	
	#Make ship
	ship =Ship(ai_settings, screen)
	
	#Create an instance to store gane stats
	stats= GameStats(ai_settings)
	scoreboard= Scoreboard(ai_settings, screen, stats, ship)
	
	#Create fleet of aliens
	aliens= Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)	
	
	#Make a group to store bullets
	bullets= Group()
	
	while True:
		gf.check_events(ai_settings, screen, ship, aliens, 
		play_button, stats, bullets, scoreboard)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_settings, 
			stats, screen, scoreboard, ship)
			gf.update_aliens(ai_settings, stats, screen, ship,
			aliens, bullets, scoreboard)
			
		gf.update_screen(ai_settings, screen, stats, scoreboard, 
		ship, aliens, bullets, play_button)
		
		
if __name__ == '__main__':	
	run_game()








