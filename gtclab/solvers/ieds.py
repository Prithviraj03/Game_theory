# Compute the reduced game using iterative elimination of dominated strategies for a given normal form game. 

from ..models.normalgame import NormalGame

class IEDS:
    
    def __init__(self, normal_game):
        # This works only for normal game representation.
        if isinstance(normal_game, NormalGame):
            self.original_game = normal_game
            self.reduced_game = normal_game
        else:
            raise RuntimeError("IEDS can only be computed for Normal games.")
        self.calc_reduced_game()
    
    def calc_reduced_game(self):
        # TODO: Implement Iterative Elimination of Dominated Strategies for basic principles (i.e. from the definition)
        # Save the reduced choice profile space and utility matrices in the following two variables:
        # reduced_C = [['a'], ['c']]
        # reduced_U = ['1', '-1']
        reduced_C = {1: 1, 2: 1}
        reduced_U = {
                1: [[1]],
                2: [[-1]]}
        # Define the reduced normal-form game using the reduced choice profile space and the reduced utility matrices
        self.reduced_game = NormalGame(self.original_game.num_players, reduced_C, reduced_U)
        
        # Define the stopping criterion
        if self.reduced_game == self.original_game: #TODO 
            # TODO: Stop the recursion only when the game does not reduce at all players.
            return self.reduced_game
        else:
            # TODO: Continue the recursion until the game can no longer be reduced. Make sure the recursion includes a round-robin iteration of the players.
            self.calc_reduced_game(self.reduced_game)

    def is_dominated(self, utility_matrix):
        raise NotImplemented('is_dominated function not implemented.')

    def __repr__(self): 
        return f"""Reduced Game due to IEDS : {self.reduced_game}\n"""