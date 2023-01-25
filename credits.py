from state import State
from v3Classes import *
from v3Constants import *

class Credits(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self,game)

        #cute images
        self.dino1 = RUNNING1[0].convert_alpha()
        self.dino2 = RUNNING2[0].convert_alpha()
        self.dino3 = RUNNING3[0].convert_alpha()

        self.dino1_rect = self.dino1.get_rect()
        self.dino1_rect.x = self.game.screen_width//4
        self.dino1_rect.y = self.game.screen_height - 300

        self.dino2_rect = self.dino2.get_rect(bottom=SCREEN_H)
        self.dino2_rect.x = SCREEN_W//2 - 150
        self.dino3_rect = self.dino3.get_rect()



    
    def update(self,clock,actions):
        if actions['tab']:
            self.game.state_stack.pop() 
        self.game.reset_keys()

    def render(self,display):
        display.fill('white')
        self.game.draw_text("C R E D I T S",50,self.game.window,self.game.screen_width//2,150)
        self.game.draw_text("Designer   Atakan",50,self.game.window,self.game.screen_width//2,200)
        self.game.draw_text("Producer   Hunter",50,self.game.window,self.game.screen_width//2,250)
        self.game.draw_text("Programmers    Oliver  and  Maddie",50,self.game.window,self.game.screen_width//2,300)
        self.game.draw_text("Visual Artist     Danny",50,self.game.window,self.game.screen_width//2,350)
        self.game.draw_text("Audio Artist     Miran",50,self.game.window,self.game.screen_width//2,400)       
        self.game.draw_text("",50,self.game.window,self.game.screen_width//2,450)

        display.blit(self.dino2, self.dino2_rect)
