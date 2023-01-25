from state import State
from v3Classes import *
from v3Constants import *
from level_one import Level_One
from level_two import Level_Two
from level_four import Level_Four
from level_three import Level_Three
from level_two import Level_Two
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

        #UNLOCK
        self.one_unlocked = True
        self.two_unlocked = False
        self.three_unlocked = False
        self.four_unlocked = False

        
        #Cursor Images
        self.cursor_image = CURSOR
        self.cursor_rect = self.cursor_image.get_rect()
        self.cursor_ypos = self.level_one.y
        self.cursor_rect.x,self.cursor_rect.y = self.level_one.x - 120, self.cursor_ypos

        #Sound
        self.move = MENU_MOVE
        self.select = MENU_SELECT

    def update(self,delta_time,actions):

        self.update_cursor(actions)
        self.check_to_unlock()
        if actions['start']:
            self.select_sound()
            self.manage_transitions()
        self.game.reset_keys()

    def render(self,display):
        #Draw buttons in this function
        display.fill('white')
        self.game.draw_text("Dino  Game",50,self.game.window,self.game.screen_width//2,150)
        
        str_score_one = "LVL 1  HIGH  SCORE   "+str(self.game.lvl_one_score)
        str_score_two = "LVL 2  HIGH  SCORE   "+str(self.game.lvl_two_score)
        str_score_three = "LVL 3  HIGH  SCORE   "+str(self.game.lvl_three_score)
        str_score_four = "LVL 4  HIGH  SCORE   "+str(self.game.lvl_four_score)

        self.game.draw_text(str_score_one,30,self.game.window,self.game.screen_width//4,350)
        self.game.draw_text(str_score_two,30,self.game.window,self.game.screen_width//4,400)
        self.game.draw_text(str_score_three,30,self.game.window,self.game.screen_width//4,450)
        self.game.draw_text(str_score_four,30,self.game.window,self.game.screen_width//4,500)


        self.game.draw_text("Use  up  and  down  keys  to  navigate  the  menu",50,self.game.window,self.game.screen_width//2,225)
        self.game.draw_text("P R E S S  E S C  T O  Q U I T",30,self.game.window,self.game.screen_width//2,275)
        display.blit(self.cursor_image,self.cursor_rect)

        #draw buttons to screen
        self.draw_buttons(display)

        self.help.draw_button(display)
        self.credits.draw_button(display)

    def manage_transitions(self):
        if self.menu_options[self.index] == "one":
            new_state = Level_One(self.game)
            new_state.enter_state()
        if self.menu_options[self.index] == "two":

            if self.two_unlocked:
                new_state = Level_Two(self.game)
                new_state.enter_state()
        if self.menu_options[self.index] == "three":
            
            if self.three_unlocked:
                new_state = Level_Three(self.game)
                new_state.enter_state()
        if self.menu_options[self.index] == "four":
            if self.four_unlocked:
                new_state = Level_Four(self.game)
                new_state.enter_state()
        if self.menu_options[self.index] == "help":
            new_state = Help(self.game)
            new_state.enter_state()
        if self.menu_options[self.index] == "credits":
            pass


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

    def draw_buttons(self,display):
        self.level_one.draw_button(display)

        if self.two_unlocked == False:
            self.level_two.draw_button(display,False)
        if self.two_unlocked == True:
            self.level_two.draw_button(display)

        if self.three_unlocked == False:
            self.level_three.draw_button(display,False)
        if self.three_unlocked == True:
            self.level_three.draw_button(display)

        if self.four_unlocked == False:
            self.level_four.draw_button(display,False)
        if self.four_unlocked == True:
            self.level_four.draw_button(display)
        
    
    
    def check_to_unlock(self):
        if self.game.lvl_one_score > 500:
            self.two_unlocked = True
        if self.game.lvl_two_score > 500:
            self.three_unlocked = True
        if self.game.lvl_three_score > 500:
            self.four_unlocked = True
        
