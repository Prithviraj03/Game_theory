import numpy as np
# from .base import player, state, tree
# from ..base.player import Player
# from ..base.state import State
# from ..base.tree import Tree

class ExtensiveGame:
    def __init__(self, tree):
        if self.is_tree_proper_extensive_game(tree):
            self.tree = tree
        else:
            raise RuntimeError("Extensive Game is not well defined.")

    def __repr__(self):
        return f"""Extensive Game :  {self.tree}"""
    
    
    def get_subgame(self, state_label):
        # TODO: Construct a game from the subtree of state.state_label.
        raise NotImplemented('get_subgame - not implemented')

    def is_tree_proper_extensive_game(self, tree):
        '''
        Criteras
        1. Every state should have a valid player defined.
        2. if state.player is not num_players+1, state.children cannot be empty.
        3. leaf node should have utilities defined.
        '''
        raise NotImplemented('is_tree_proper_extensive_game - not implemented')
    
