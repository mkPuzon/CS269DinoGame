from state import State
from v3Classes import *
from v3Constants import *
from pause import Pause
from game_over import Game_Over

class Level_Three(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self,game)
        self.music = WWI_MUSIC
        self.music.play(loops=-1)

        #points variable
        self.points = 0

        #group initialization
        self.player_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()

        #Player Initialization
        self.player = Player_3(self.player_group)
        self.game_speed = 14

        #Ground Initialization
        self.x_pos_bg = 0
        self.y_pos_bg = GROUND_LOCATION + 100
        self.ground_img = GROUND2.convert_alpha()
        self.ground_image_width = self.ground_img.get_width()
        #Backdrop  Initialization
        self.backdrop_img = BACKDROP2.convert_alpha()
        self.backdrop_image_width = self.backdrop_img.get_width()
        self.x_pos_backdrop = 0
        self.y_pos_backdrop = 115
    
    def update(self,clock,actions):
        if actions['tab']:
            new_state = Pause(self.game)
            new_state.enter_state()

        self.update_speed()
        self.player.update(actions)
        self.check_collision()
        self.generate_obstacles()
        self.update_obstacles(self.game_speed)
        

        # self.game.reset_keys()
        clock.tick(30)

    def render(self,display):
        display.fill('white')
        self.move_backdrop(display)
        self.move_ground(display)
        self.player.render_player(display)
        self.render_obstacles(display)

    def move_ground(self,display):
        display.blit(self.ground_img, (self.x_pos_bg, self.y_pos_bg))
        display.blit(self.ground_img, (self.x_pos_bg + self.ground_image_width, self.y_pos_bg))
        if self.x_pos_bg <= -self.ground_image_width:
            display.blit(self.ground_img, (self.ground_image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def move_backdrop(self,display):

        display.blit(self.backdrop_img, (self.x_pos_backdrop, self.y_pos_backdrop))
        display.blit(self.backdrop_img, (self.backdrop_image_width + self.x_pos_backdrop, self.y_pos_backdrop))
        if self.x_pos_backdrop <= -self.backdrop_image_width:
            display.blit(self.backdrop_img, (self.backdrop_image_width + self.x_pos_backdrop, self.y_pos_backdrop))
            self.x_pos_backdrop = 0
        self.x_pos_backdrop -= (self.game_speed * 0.2)
    
    def update_speed(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
    
    def generate_obstacles(self):
        if len(self.obstacle_group) == 0:
            if randint(0,2) == 0:
                new_obst = Mine2(SMALL_OBST2,self.obstacle_group)
            elif randint(0,2) == 1:
                new_obst = GroundObstacle(LARGE_OBST2[randint(0,2)],self.obstacle_group)
                new_obst2 = Mine2(SMALL_OBST2,self.obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,2) == 2:
                new_obst = FlyingObstacle2(FLYING_OBST2,self.obstacle_group)
                new_obst2 = GroundObstacle(LARGE_OBST2[randint(0,2)],self.obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(400,1000)
            elif randint(0,1) == 1:
                new_obst = FlyingObstacle2(FLYING_OBST2,self.obstacle_group)
                new_obst2 = Mine2(SMALL_OBST2,self.obstacle_group)
                new_obst2.rect.x = new_obst.X_POS + randint(300,2000)

    def update_obstacles(self,game_speed):
        for obstacle in self.obstacle_group:
            obstacle.update(game_speed)
        
    def render_obstacles(self,display):
        for obstacle in self.obstacle_group:
            obstacle.draw(display)

    def check_collision(self):
        # for obstacle in self.obstacle_group:
        #     # check collisions
        #     overlap_area = self.player.mask.overlap_area(obstacle.mask, (obstacle.rect.x - self.player.rect.x, obstacle.rect.y - self.player.rect.y))

        if pygame.sprite.spritecollide(self.player,self.obstacle_group,False,pygame.sprite.collide_mask):
            DEATH_SOUND.play()
            pygame.mixer.stop()
            # death_count += 1
            pygame.time.delay(2000)
            for obstacle in self.obstacle_group:
                    obstacle.kill()

            pygame.mixer.stop()

                    #interem return to menu
            self.game_over()

    def game_over(self):
        #load new state here
        pygame.mixer.stop()
        self.check_score_lv3()
        new_state = Game_Over(self.game)
        new_state.enter_state()

    def get_score(self):
        return self.points

    def check_score_lv3(self):
        if self.points > self.game.lvl_three_score:
           self.game.lvl_three_score = self.points
    def render_score(self, display):
        self.game.draw_text('Score  ' + str(self.points),30,display,display.get_width()- 200,100)