from state import State
from v3Classes import *
from v3Constants import *

class Help(State):
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

        self.dino2_rect = self.dino2.get_rect()
        self.dino3_rect = self.dino3.get_rect()



    
    def update(self,clock,actions):
        if actions['tab']:
           while len(self.game.state_stack) > 1:
                self.game.state_stack.pop() 
        self.game.reset_keys()

    def render(self,display):
        display.fill('white')
        self.game.draw_text("H E L P",50,self.game.window,self.game.screen_width//2,150)
        self.game.draw_text("PRESS  TAB  TO  RETURN  TO  MENU   FROM   HELP",50,self.game.window,self.game.screen_width//2,200)
        self.game.draw_text("IN A LEVEL PRESS  TAB  TO PAUSE",50,self.game.window,self.game.screen_width//2,250)
        self.game.draw_text("PRESS  ESCAPE  TO  QUIT  THE  GAME",50,self.game.window,self.game.screen_width//2,300)
        self.game.draw_text("UP ARROW TO JUMP DOWN ARROW TO DUCK SPACE TO SHOOT",50,self.game.window,self.game.screen_width//2,350)
        self.game.draw_text("PRESS  ENTER  TO  SELECT  A  BUTTON",50,self.game.window,self.game.screen_width//2,400)

        display.blit(self.dino1, self.dino1_rect)


        