# Compute pure strategy minimax equilibrium for a 2-player, zero-sum normal form game. 
import numpy as np
from ..models.normalgame import NormalGame

class PSME:
    
    def __init__(self,normal_game):
        # This works only for Two Player Zero Sum Normal game representation.
        if (isinstance(normal_game, NormalGame) and normal_game.is_two_player_zero_sum()):
            self.game = normal_game
        else:
            raise RuntimeError("PSME can only be computed for Two Player Zero Sum Normal games.")
        self.psme = None
        self.calc_psme()
    
    def calc_psme(self):
        # TODO: Implement Pure Strategy Minimax Equilibrium (i.e. from the definition)
        raise NotImplemented("calc_psmet is not implemented.") #Comment this line after this function is implemented and return self.psme
    
    def __repr__(self): 
        return f"""PSME : {self.psme}\
        \n"""