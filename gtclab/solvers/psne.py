# Compute pure strategy Nash equilibrium for a given normal form game. 
import numpy as np

from ..models.normalgame import NormalGame

class PSNE:
    
    def __init__(self, normal_game):
        # This works only for normal game representation.
        if isinstance(normal_game, NormalGame):
            self.normal_game = normal_game
        else:
            raise RuntimeError("PSNE can only be computed for Normal games.")
        self.psne = None
        self.calc_psne()
    
    def calc_psne(self):
        # TODO: Calculate and return PSNE for basic principles (i.e. from the definition)
        # Save the PSNE in the following format. If there is no PSNE, return 'None' and print "This game has no PSNE"
        # self.psne = ['(Game.player[1].choice_set[1], ..., Game.player[n].choice_set[1])']
        raise NotImplemented("calc_psne is not implemented.") #Comment this line after this function is implemented and return self.psne

    def is_best_response(self):
        '''
        Given all other players' choices, check if a given choice of a given player is a best response strategy.
        '''
        raise NotImplemented('is_best_response function not implemented.')
    
    def __repr__(self): 
        return f"""PSNE : {self.psne}\
        \n"""