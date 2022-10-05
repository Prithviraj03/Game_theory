from .state import State
from .player import Player

class Tree:
    def __init__(self, states={}):
        self.states = states # This is a dictionary of states. key: state_label, value: state obj
        
        self.num_players = 1

        self.players = []
        for n in range(self.num_players+2):
            player = Player(n)
            self.players.append(player)
    
    
    def __repr__(self):
        state_str = f'Tree : '
        if self.states: 
            state_str += f'\n States: {self.states}\n'
        return state_str
    
    def create_state(self, state_label):
        raise NotImplemented('create_state - create a new state not implemented')

    def add_state(self,state_obj):
        raise NotImplemented('add_state - add a state not implemented')
    
    def get_state(self, state_label):
        raise NotImplemented('get_state - get a state not implemented')

    def add_player(self, player_label):
        raise NotImplemented('add_player - not implemented')

    def check_player_exists(self, player_label):
        raise NotImplemented('check_player_exists - not implemented')

    def add_player_to_state(self, player_label, state_obj):
        raise NotImplemented('add_player_to_state - not implemented')

    def set_num_players(self, num_players):
        #update num_players count and automatically create player objects
        raise NotImplemented('set_num_players - not implemented')
    
    def get_num_players(self):
        raise NotImplemented('get_num_players - not implemented')

    def set_root(self, state_label):
        raise NotImplemented('set_root - not implemented')

    def get_root(self):
        raise NotImplemented('get_root - not implemented')
    
    def is_parent(self, parent_state_label, child_state_label):
        raise NotImplemented('is_parent - not implemented')

    def set_child(self, parent_state_label, child_state_label):
        raise NotImplemented('set_child - not implemented')

    def get_children(self, state_label):
        raise NotImplemented('get_child - not implemented')

    def is_leaf(self, state_label):
        raise NotImplemented('is_leaf - not implemented')

    def set_utilities(self, state_label, utilities):
        raise NotImplemented('set_utilities - not implemented')

    def get_utilities(self, state_label):
        raise NotImplemented('get_utilities - not implemented')
    
    def set_chance_prob(self, state_label, chance_prob):
        raise NotImplemented('set_chance_prob - not implemented')
    
    def get_chance_prob(self,state_label):
        raise NotImplemented('get_chance_prob - not implemented')
