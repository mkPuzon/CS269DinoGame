from state import State
from v3Classes import *
from v3Constants import *


class Game_Over(State):
    def __init__(self,game):
        self.game = game
        State.__init__(self,game)
        
        self.menu_options = {0:'retry',1:'menu'}
        self.index = 0

        #BUTTONS
        self.retry = Button(self.game.screen_width//2,300+(80*0),200,70,'R E T R Y')
        self.menu = Button(self.game.screen_width//2,300+(80*1),200,70,'M E N U')

        #Cursor INIT
        self.cursor_image = CURSOR
        self.cursor_rect = self.cursor_image.get_rect()
        self.cursor_ypos = self.retry.y
        self.cursor_rect.x,self.cursor_rect.y = self.retry.x - 120, self.cursor_ypos

        self.move = MENU_MOVE
        self.select = MENU_SELECT

    def update(self,delta_time,actions):
        self.update_cursor(actions)
        if actions['start']:
            self.select_sound()
            self.manage_transitions()
        self.game.reset_keys()
    
    def render(self,display):
        #Draw buttons in this function
        display.fill('white')
        self.game.draw_text("Game   Over",50,self.game.window,self.game.screen_width//2,150)
        
        prev_score = self.game.state_stack[-2].get_score()
        prev_score_string = str(prev_score)
        score = "SCORE    "+prev_score_string
        self.game.draw_text(score,50,self.game.window,self.game.screen_width//2,225)
        
        display.blit(self.cursor_image,self.cursor_rect)

        self.retry.draw_button(display)
        self.menu.draw_button(display)

    def manage_transitions(self):
        if self.menu_options[self.index] == "retry":
            self.exit_state()
        if self.menu_options[self.index] == "menu":
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()

    def update_cursor(self,actions):
        if actions['up']:
            self.index = (self.index - 1) % len(self.menu_options)
            self.move_sound()
        if actions['down']:
            self.index = (self.index + 1) % len(self.menu_options)
            self.move_sound()
        self.cursor_rect.y = self.cursor_ypos + (self.index *80)

    def move_sound(self):
        pygame.mixer.Sound.play(self.move)

    def select_sound(self):
        pygame.mixer.Sound.play(self.select)

