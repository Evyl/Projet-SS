##from soccersimulator import Vector2D
#v= Vector2D(x=2.,y=1.)
#v_bis= Vector2D(angle= 3, norm = 2)
#print v_bis
import soccersimulator
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament
from soccersimulator import AbstractStrategy, Vector2D, SoccerAction
class MaStrategy(AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self, "meow")
        # rajouter l’initialisation voulue
    def compute_strategy(self, state, id_team, id_player):
        if (id_team==2):
            #### rajouter du code, renvoyer un SoccerAction
            p = state.player_state(id_team, id_player)
            return SoccerAction(state.ball.position - p.position, Vector2D((150-state.ball.position.x),(45-state.ball.position.y)))
        elif (id_team==1):
             #### rajouter du code, renvoyer un SoccerAction
            p = state.player_state(id_team, id_player)
            return SoccerAction(state.ball.position - p.position, Vector2D((0-state.ball.position.x),(45-state.ball.position.y)))

team1 = SoccerTeam("team1",[Player("t1j1",MaStrategy())])
team2 = SoccerTeam("team2",[Player("t2j1",MaStrategy())])
team3 = SoccerTeam("team3", [Player("t3j1", MaStrategy())])
match = SoccerMatch(team1, team2)

soccersimulator.show(match)
