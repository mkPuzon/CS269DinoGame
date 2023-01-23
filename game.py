import os, time,pygame
from sys import exit
from v3Constants import *
from v3Classes import *
from random import randint

from title_screen import Title

class Game():
    def __init__(self):
      pygame.init()
      self.running = True
      self.playing = True
      self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
      self.screen_width = self.window.get_width() 
      self.screen_height = self.window.get_height()
      self.display = pygame.Surface((self.screen_width,self.screen_height))
      #Below is a dictionary that tracks user keyboard input
      self.actions = {'up':False,'down':False,'start':False,'escape':False,'back':False,'space': False,'tab':False}
      self.font = 'Assets/ARCADECLASSIC.TTF'
      self.dt, self.prev_time = 0,0
      self.BLACK,self.WHITE = (0,0,0),(255,255,255)
      #This is a stack that keeps track of the game states

      #initialize gamespeed
      self.clock = pygame.time.Clock()
      self.state_stack = []
      self.load_assets()
      self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.process_events()
            self.update()
            self.render()
            
            #self.display.fill(self.WHITE)
            #visible stuff goes below here
            #self.draw_text("TEST",30,self.screen_width//2, self.screen_height//2)
            #self.window.blit(self.display,(0,0))
            #pygame.display.update()
            # self.reset_keys()


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False,False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True
                if event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = True
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = True
                if event.key == pygame.K_TAB:
                    self.actions['tab'] = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC = True
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False
                if event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = False
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = False
                if event.key == pygame.K_TAB:
                    self.actions['tab'] = False
                   

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
        
    
    def draw_text(self, text,size,display, x,y):
    
        font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', size)
        text_surface = font.render(text,True,self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        display.blit(text_surface,text_rect)
    
    def update(self):
        self.state_stack[-1].update(self.clock,self.actions)

    def render(self):
        self.state_stack[-1].render(self.window)
        pygame.display.update()
    
    def load_assets(self):
        '''will create pointers to the image and font filepaths'''
        self.font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30)
    
    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    
    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()