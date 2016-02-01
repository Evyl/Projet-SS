class PlayerStateDecorator:
def __init__(self,state,idteam,idplayer):
self.state = state
self.idteam = idteam
self.idlpayer = idplayer
def position(self):
return self.state.player_state(idteam,idplayer).position
def distance_ball(self):
return self.state.ball_position.distance(self.position())
