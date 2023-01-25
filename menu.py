import pygame
from game import Game
from v3Constants import MENU_MUSIC

class Menu():
    def __init__(self,game):
        g = Game()
        self.game = g
        self.mid_w = self.game.screen_width/2
        self.mid_h = self.game.screen_height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
    
    def draw_cursor(self):
        self.game.draw_text("*",15,self.cursor_rect.x,self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        self.state = "Start"
        
        self.start_x,self.start_y = self.mid_w,self.mid_h+30
        self.options_x,self.options_y = self.mid_w,self.mid_h+50
        self.credits_x, self.credits_y = self.mid_w, self.mid_h+70
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.process_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text("Main Menu",20,self.game.screen_width/2,self.game.screen_height/2 - 20)
            self.game.draw_text("Start Game",20,self.start_x,self.start_y)
            self.game.draw_text("Options",20,self.options_x,self.options_y)
            self.game.draw_text("Credits",20,self.credits_x,self.credits_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            if self.state == 'Credits':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
            if self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
    
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False
