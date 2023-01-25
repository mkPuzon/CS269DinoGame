from state import State
from v3Classes import *
from v3Constants import *

class Pause(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self,game)

        self.menu_options = {0:'cont',1:'help',2:'title'}
        self.index = 0
    
        self.cont = Button(self.game.screen_width//2,300+(80*0),200,70,'CONTINUE')
        self.help = Button(self.game.screen_width//2,300+(80*1),200,70,'H E L P')
        self.title = Button(self.game.screen_width//2,300+(80*2),200,70,'M E N U')


        #cursor set up
        self.cursor_image = CURSOR
        self.cursor_rect = self.cursor_image.get_rect()
        self.cursor_ypos = self.cont.y
        self.cursor_rect.x,self.cursor_rect.y = self.cont.x - 120, self.cursor_ypos

        self.move = MENU_MOVE
        self.select = MENU_SELECT

    def update(self,delta_time,actions):
        
        self.update_cursor(actions)
        if actions['start']:
            self.select_sound()
            self.manage_transitions()
        self.game.reset_keys()

    def render(self,display):
        display.fill('white')
        self.game.draw_text("PAUSE MENU",50,self.game.window,self.game.screen_width//2,150)

        display.blit(self.cursor_image,self.cursor_rect)

        self.cont.draw_button(display)
        self.help.draw_button(display)
        self.title.draw_button(display)

    def update_cursor(self,actions):
        if actions['up']:
            self.move_sound()
            self.index = (self.index - 1) % len(self.menu_options)
        if actions['down']:
            self.move_sound()
            self.index = (self.index + 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_ypos + (self.index *80)
    
    def manage_transitions(self):
        if self.menu_options[self.index] == "cont":
            self.exit_state()
        elif self.menu_options[self.index] == 'help':
            pass
        elif self.menu_options[self.index] == 'title':
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()
    
    def move_sound(self):
        pygame.mixer.Sound.play(self.move)

    def select_sound(self):
        pygame.mixer.Sound.play(self.select)