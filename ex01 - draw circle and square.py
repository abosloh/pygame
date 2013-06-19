#!/usr/bin/env python

####################
# by : abosloh
# email : abosloh.654@gmail.com
# homepage : https://github.com/abosloh
#
#####################

import pygame , sys
from pygame.locals import *
from random import randint

class main():
    
    size = (640,480) # size window
    
    shapes = [] # shapes
    
    # colors
    color = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),
             (255,0,255),(192,192,192),(128,128,128),(128,0,0),(128,128,0),(0,128,0),
             (128,0,128),(0,128,128),(0,0,128)]    
    
    # type of shape
    type_shape = ["circle" , "square"]
    
    def __init__(self):
        pygame.init()# initialise pygame
        
        self.screen = pygame.display.set_mode( self.size , 0,32 ) # set display
        
        self.clock = pygame.time.Clock() # create an object to help track time 
    
    # handle keys
    def handle_key(self , keys):
        
        # if click escape exit from window
        if keys[K_ESCAPE]:
            self.exit()
    
    # handle event
    def handle_event(self , events):
        
        for event in events:
            # if click QUIT exit from window
            if event.type == QUIT:
                self.exit()
            
            # if pressed mouse create shape circle or square
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                self.shapes.append([ self.color[ randint( 0 , len(self.color)-1 ) ] , pygame.mouse.get_pos() , 0 , self.type_shape[ randint( 0 , len(self.type_shape)-1 ) ]])
    
    # draw   
    def draw(self):
        
        for shape in self.shapes:
            # if size greater than 100 remove shape from shapes
            if shape[2] > 100: 
                self.shapes.remove(shape)
                continue
            
            # draw circle 
            if shape[3] == "circle":
                pygame.draw.circle(self.screen , shape[0] , shape[1] , shape[2])
                shape[2] += 1
            
            # draw square
            if shape[3] == "square":
                pygame.draw.rect(self.screen , shape[0] , pygame.Rect( (shape[1][0]-shape[2] , shape[1][1]-shape[2]) , (shape[2]*2,shape[2]*2) ) )
                shape[2] += 1
    
    # clean window
    def clean(self):
        self.screen.fill((60,60,60))
    
    # update window
    def update(self):
        self.clock.tick(50)
        pygame.display.flip()
    
    # run
    def run(self):
        while True:
            self.clean() # call clean method
            self.handle_event(pygame.event.get()) # call handle event method
            self.handle_key(pygame.key.get_pressed()) # call handle key method
            self.draw() # call draw method
            self.update() # call update method
            
        self.exit()
    
    # exit
    def exit(self):
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    main = main()
    main.run()
