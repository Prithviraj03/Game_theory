# Compute mixed strategy minimax equilibrium for a 2-player, zero-sum normal form game. 
import numpy as np
from ..models.normalgame import NormalGame


class MSME:
    
    def __init__(self, normal_game):
        # This works only for Two Player Zero Sum Normal game representation.
        if (isinstance(normal_game, NormalGame) and normal_game.is_two_player_zero_sum()):
            self.game = normal_game
        else:
            raise RuntimeError("MSME can only be computed for Two Player Zero Sum Normal games.")
        self.msme = None
        self.calc_msme()
    
    def calc_msme(self):
        # TODO: Implement Mixed Strategy Nash Equilibrium using LP Solvers (i.e. from the definition)
        # Save the mixed strategy equilibrium in the following format:
        self.msme = np.array([[0.5, 0.2, 0.3], [0.1, 0.45, 0.45]])
        raise NotImplemented("calc_msme is not implemented.") #Comment this line after this function is implemented and return self.msme
    
    def __repr__(self): 
        return f"""MSME : {self.msme}\
        \n"""

