import math
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import SoccerTournament, SoccerTeam, SoccerMatch, Player, show
from soccersimulator.settings import *
from soccersimulator import BaseStrategy

###Creation de strategie

class fonceetshoot(BaseStrategy):
        def __init__(self,name="ma strategie"):
                         BaseStrategy.__init__(self,name)
        def compute_strategy(self,state,idteam,idplayer):
                if idteam==2:
                        p = state.player_state(idteam, idplayer)
                        return SoccerAction(state.ball.position - p.position, Vector2D((GAME_WIDTH-state.ball.position.x),(GAME_HEIGHT/2-state.ball.position.y)))
                elif idteam==1:
                        p = state.player_state(idteam, idplayer)
                        return SoccerAction(state.ball.position - p.position, Vector2D((0-state.ball.position.x),(GAME_HEIGHT/2-state.ball.position.y)))


class defenseduGoal(BaseStrategy):
        def __init__(self,name="ma strategie"):
                        BaseStrategy.__init__(self,name)

        
        def compute_strategy(self,state,idteam,idplayer):
                p = state.player_state(idteam, idplayer)
               
                if state.ball.position.x<40:
                        return SoccerAction(state.ball.position - p.position, Vector2D(GAME_WIDTH-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if state.ball.position.x>110:
                        return SoccerAction(state.ball.position - p.position, Vector2D(0-state.ball.position.x,GAME_HEIGHT/2-state.ball.position.y))
                if idteam==2:
                        p.position=Vector2D(0,GAME_HEIGHT/2)
                        p = state.player_state(idteam, idplayer)
                        if((p.position.x>5) and (p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT) or (p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
                                p.position = Vector2D(0,GAME_HEIGHT/2)
                                return p.position
                if idteam==1:
                        p.position=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
                        p = state.player_state(idteam, idplayer)
                        if((p.position.x<95)and(p.position.y>GAME_HEIGHT/2+GAME_GOAL_HEIGHT)or(p.position.y<GAME_HEIGHT/2-GAME_GOAL_HEIGHT)):
                                p.position = Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
                                return p.position


