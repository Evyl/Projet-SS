from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTournament, SoccerTeam, SoccerMatch, Player, show
from soccersimulator import BaseStrategy
from soccersimulator.settings import *
from Strategiecode1 import fonceetshoot, defenseduGoal
import math
## Creation joueur et equique (2 joueurs)

Joueur1 = Player("Joueur 1", fonceetshoot("fonceetshoot"))
Goal1 = Player("Goal 1", defenseduGoal("defenseduGoal"))
print Joueur1.name, Joueur1.strategy, Goal1.name, Goal1.strategy
team1 = SoccerTeam("Equipe 1", [Joueur1, Goal1])
# nombre de joueurs de l equipe
print team1.nb_players
# renvoie la liste des noms, la liste des strategies
print team1.players_name, team1.strategies
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)

Joueur2 = Player("Joueur 2", fonceetshoot("fonceetshoot"))
Goal2 = Player("Goal 2", defenseduGoal("defenseduGoal"))
print Joueur2.name, Joueur2.strategy, Goal2.name, Goal2.strategy
team2 = SoccerTeam("Equipe 2", [Joueur2, Goal2])
# nombre de joueurs de l equipe
print team1.nb_players
# renvoie la liste des noms, la liste des strategies
print team1.players_name, team1.strategies
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)
