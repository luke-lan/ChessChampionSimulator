#!/usr/bin/env python

"""Youtube audio and subtitles downloader"""
__author__ = "Luke Lancaster"
__copyright__ = "Copyright (c) 2018, Luke Lancaster"

__license__ = "MIT"
__version__ = "0.1.1"
__email__ = "lancaster.lucas.a@gmail.com"
__status__ = "Submitted"

from random import choices

win_chance = 20
lose_chance = 15
draw_chance = 65

# Up to how many games to play per match
num_games = 25
# How many simulations to run
num_runs = 10000

# What win percentage for better player are you hoping for?
win_target = 99

def match_sim():
  # Vary num games per match
  for i in range(num_games):
      wins = 0
      losses = 0
      draws = 0
      # Run a bunch of trials
      for j in range(num_runs):
          points = sum(
              choices([1, 0, 0.5], [win_chance, lose_chance, draw_chance], k=i))
          if points >= 6.5:
              wins += 1
          elif points < 6:
              losses += 1
          elif points == 6:
              draws += 1

      if (wins / num_runs * 100) > win_target:
          print("Won {}% of matches when playing {} games per match".format(wins / num_runs * 100, i))

if __name__ == "__main__":
  match_sim()
