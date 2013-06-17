#!/usr/bin/env python

import pygame , sys
from pygame.locals import *

class Game():
    
    SIZE = (640,480)
    
    RUNNING = True
    
    # initialise
    def __init__(self):
        
        
        pygame.init() # initialise pygame
        
        self.screen = pygame.display.set_mode(self.SIZE , 0 , 32) # create screen
        
        self.Clock = pygame.time.Clock() # create an object to help track time 
        
        self.x_rect, self.y_rect = 0,450    # position rectangle
        self.w_rect, self.h_rect = 100,15   # size rectangle
        self.speed_rect = 10    # speed movement rectangle
        
        self.r_circ = 30                                        # radius circle
        self.x_circ, self.y_circ = self.r_circ+1,self.r_circ+1  # position circle
        
        self.speed_circ = 1 # speed movement circle 
        
        self.y_move_circ = 1 # move circle up = -1 , move circle down = 1
        self.x_move_circ = 1 # move circle left = -1 , move circle right = 1  
        
        
    # handle all keys pressed
    def handle_keys(self,keys):
        
        # if pressed ESCAPE 
        if keys[K_ESCAPE]:
            self.exit()
        
        # move rect right-left
        if keys[K_RIGHT]:
            self.x_rect += self.speed_rect
        if keys[K_LEFT]:
            self.x_rect -= self.speed_rect
        
    # handle for all events
    def handle_events(self, events):
        
        for event in events:
                
                # quit
                if event.type == QUIT:
                    self.exit()
                
                # motion mouse
                if event.type == pygame.MOUSEMOTION:
                    self.pos = pygame.mouse.get_pos()
                    self.x_rect = pygame.mouse.get_pos()[0] - (self.w_rect/2)
                        
    
    # clear screen
    def clear_screen(self):
        self.screen.fill((0,200,237))
    
    # update screen
    def update_screen(self):
        self.Clock.tick(50)     # update the clock by framerate
        pygame.display.flip()
    
    # draw rectangle
    def draw(self):
        
        self.rect = pygame.draw.rect( self.screen , (0,0,0) , pygame.Rect((self.x_rect,self.y_rect),(self.w_rect,self.h_rect)) ) # draw Rectangle
        self.circ = pygame.draw.circle(self.screen , (0,0,0) , (self.x_circ,self.y_circ) , self.r_circ )
                
    # run
    def run(self):
        
        while self.RUNNING == True:
            
            self.clear_screen()                         # clear screen
            self.handle_events(pygame.event.get())      # handle events
            self.handle_keys(pygame.key.get_pressed())  # handle keys
            
            self.draw() # draw
            
            # move circle up-down
            if self.y_move_circ == 1 and self.circ.bottom > self.rect.top and ( self.rect.left <= self.circ.right <= self.rect.right or self.rect.left < self.circ.left < self.rect.right ):
                self.y_move_circ = -self.y_move_circ
            if self.circ.top <= 0:
                self.y_move_circ = -self.y_move_circ
            
            
            # move circle right-left 
            if self.circ.left <= 0 or self.circ.right >= self.SIZE[0] :
                self.x_move_circ = -self.x_move_circ
            
            self.y_circ += self.speed_circ * self.y_move_circ # reset position circle y
            self.x_circ += self.speed_circ * self.x_move_circ # reset position circle x
            
            # game over
            if self.circ.bottom >= self.SIZE[1]:
                self.RUNNING = False
            
            self.update_screen() # update screen
        
        self.exit()
    
    
    # exit
    def exit(self):
        pygame.quit()
        sys.exit()
    
            
if __name__ == '__main__':
    Game = Game()
    Game.run()
