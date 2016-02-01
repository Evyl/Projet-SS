from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTournament, SoccerTeam, SoccerMatch, Player, show
from soccersimulator import BaseStrategy
from soccersimulator.settings import *
from Strategiecode1 import fonceetshoot, defenseduGoal
import math

## Creation joueur et equique (2 joueurs)

joueur1 = Player("Joueur 1", BaseStrategy("fonceetshoot"))
joueur2 = Player("Goal 1", BaseStrategy("defenseduGoal"))
print joueur1.name, joueur2.strategy, joueur2.name, joueur2.strategy
team1 = SoccerTeam("Equipe 1", [Joueur 1, Goal 1])
# nombre de joueurs de l equipe
print team1.nb_players
# renvoie la liste des noms, la liste des strategies
print team1.players_name, team1.strategies
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)

joueur1 = Player("Joueur 2", BaseStrategy("fonceetshoot"))
joueur2 = Player("Goal 2", BaseStrategy("defenseduGoal"))
print joueur1.name, joueur2.strategy, joueur2.name, joueur2.strategy
team2 = SoccerTeam("Equipe 2", [Joueur 2, Goal 2])
# nombre de joueurs de l equipe
print team1.nb_players
# renvoie la liste des noms, la liste des strategies
print team1.players_name, team1.strategies
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)

#Creer un match entre 2 equipes et de duree 2000 pas
match = SoccerMatch(team1, team2, 2000)
#Jouer le match (sans le visualiser)
match.play()
#Jouer le match en le visualisant
show(match)
#Attention !! une fois le match joue, la fonction play() permet de faire jouer le replay
# mais pas de relancer le match !!!
# Pour regarder le replay d un match
show(match)
# Pour sauvegarder un match
match.save("fichier")
# Pour charger un match
match = SoccerMatch.load("fichier")
# Pour reinitialiser un match
match.reset()
