from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTournament, SoccerTeam, SoccerMatch, Player, show
from soccersimulator import BaseStrategy
from soccersimulator.settings import *
from Strategiecode1 import fonceetshoot, defenseduGoal
import math
from Team import team1, team2

#Creer un match entre 2 equipes et de duree 2000 pas
match = SoccerMatch(team1, team2, 2000)
#Jouer le match (sans le visualiser)
match.play()
#Jouer le match en le visualisant
show(match)
# Pour regarder le replay d un match
show(match)
# Pour sauvegarder un match
match.save("fichier")
# Pour charger un match
match = SoccerMatch.load("fichier")
# Pour reinitialiser un match
match.reset()
