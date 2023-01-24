from state import State
from v3Classes import *
from v3Constants import *
from level_one import Level_One
from help import Help

class Title(State):
    def __init__(self,game):
        self.game = game
        State.__init__(self,game)
        
        self.menu_options = {0:'one',1:'two',2:'three',3:'four',4:'help',5:'credits'}
        self.index = 0

        #BUTTONS
        self.level_one = Button(self.game.screen_width//2,300+(80*0),200,70,'LEVEL  ONE')
        self.level_two = Button(self.game.screen_width//2,300+(80*1),200,70,'LEVEL  TWO')
        self.level_three = Button(self.game.screen_width//2,300+(80*2),200,70,'LEVEL THREE')
        self.level_four = Button(self.game.screen_width//2,300+(80*3),200,70,'LEVEL FOUR')
        self.help = Button(self.game.screen_width//2,300+(80*4),200,70,'HELP')
        self.credits = Button(self.game.screen_width//2,300+(80*5),200,70,'CREDITS')
        
        #Cursor Images
        self.cursor_image = CURSOR
        self.cursor_rect = self.cursor_image.get_rect()
        self.cursor_ypos = self.level_one.y
        self.cursor_rect.x,self.cursor_rect.y = self.level_one.x - 120, self.cursor_ypos

        

    def update(self,delta_time,actions):
        self.update_cursor(actions)
        if actions['start']:
            self.manage_transitions()
        self.game.reset_keys()

    def render(self,display):
        #Draw buttons in this function
        display.fill('white')
        self.game.draw_text("Dino  Game",50,self.game.window,self.game.screen_width//2,150)
        self.game.draw_text("Use  up  and  down  keys  to  navigate  the  menu",50,self.game.window,self.game.screen_width//2,225)
        
        display.blit(self.cursor_image,self.cursor_rect)

        #draw buttons to screen
        self.level_one.draw_button(display)
        self.level_two.draw_button(display)
        self.level_three.draw_button(display)
        self.help.draw_button(display)
        self.level_four.draw_button(display)
        self.credits.draw_button(display)

    def manage_transitions(self):
        if self.menu_options[self.index] == "one":
            new_state = Level_One(self.game)
            new_state.enter_state()
        if self.menu_options[self.index] == "two":
            pass
        if self.menu_options[self.index] == "three":
            pass
        if self.menu_options[self.index] == "four":
            pass
        if self.menu_options[self.index] == "help":
            new_state = Help(self.game)
            new_state.enter_state()
        if self.menu_options[self.index] == "credits":
            pass


    def update_cursor(self,actions):
        if actions['up']:
            self.index = (self.index - 1) % len(self.menu_options)
        if actions['down']:
            self.index = (self.index + 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_ypos + (self.index *80)