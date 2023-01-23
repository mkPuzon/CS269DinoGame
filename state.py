
class State():
    def __init__(self,game):
        self.game = game
        self.prev_state = None
    
    def update(self,clock,actions):
        pass
    
    def render(self,surface):
        pass
    
    def enter_state(self):
        '''pushs this state on to the state stack'''
        if(len(self.game.state_stack) > 1):
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
        
    
    def exit_state(self):
        '''pops the game off of the state stack'''
        self.game.state_stack.pop()
    