import pygame
from Block import *
from keyandcover import *
from Frame import *

if(__name__ == "__main__"):
    pygame.init()
    window_size = window_width, window_height = 1080,800
    window = pygame.display.set_mode(window_size,pygame.RESIZABLE)
    pygame.display.set_caption("Game by Zhao")
    clock = pygame.time.Clock() #create object to keep track of time
    frames_per_sec = 100

    stage = Frame(window_width, window_height,(3*window_width,window_height)) #This is the stage



    block_group = pygame.sprite.Group() #draw these blocks    

    platformblock=Block([0,0,0],256,32,1)                      #-----| TEMPORARY
    platformblock.set_position(10,window_height-256)           #-----| DELETE LATER

    pb1=Block([100,100,100],100,50,0.5)                      #-----| TEMPORARY
    pb1.set_position(410,window_height-500)                  #-----| DELETE LATER
    block_group.add(pb1)                             #add into a group #SPEED OF SUPPORTING OBJECTS ARE ALWAYS A FRACTION OF THE 'MAIN OBJECT'
    block_group.add(platformblock)                   #add into a group #SPEED OF SUPPORTING OBJECTS ARE ALWAYS A FRACTION OF THE 'MAIN OBJECT'

    #MAIN OBJECT: Overall speed probably kept under keyandcover so that all blocks can use their fraction to get their speed

    a_block=Block()
    a_block.set_position(window_width/2-a_block.rect.width/2,window_height/8)
    block_group.add(a_block)


    gravity=.2 #positive b/c grid is flipped upside down
    control = keyandcover()

    while(control.getrunning()):
        for event in pygame.event.get():
            control.event_(event)
        # onplatform=pygame.sprite.collide_rect(a_block,platformblock) and a_block.rect.y+a_block.height>=platformblock.rect.y and a_block.rect.y+a_block.height<platformblock.rect.y+5 #need to include similar check to move function to generalize
        # underplatform=pygame.sprite.collide_rect(a_block,platformblock) and a_block.rect.y<=platformblock.rect.y+platformblock.height and a_block.rect.y>platformblock.rect.y+platformblock.height-20
        # if(onplatform):
        #     a_block.set_position(a_block.rect.x,platformblock.rect.y-a_block.height)
        #     control.setvert(0)
        # elif(underplatform):
        #     a_block.set_position(a_block.rect.x,platformblock.rect.y+platformblock.height)
        #     control.setvert(0)
        # if(control.get_w() and (a_block.height+a_block.rect.y==window_height or onplatform)):#if w is pressed and is on a platform
        control.accelerate()    
        if(control.get_w() and (a_block.height+a_block.rect.y>=window_height)):#if w is pressed and is on a platform
            control.setvert(-10)
            didimove=a_block.move_ypos(-1,window_height)
            if(didimove):
                a_block.changecolor()
        if(control.get_a()):
            didimove=a_block.move_xpos(1,control)
            platformblock.move_xpos(1,control)
            pb1.move_xpos(1,control)
            if(didimove):
                a_block.changecolor()
        #include horizontal acceleration somewhere
        if(control.get_s()):#if on a platform
            #duck
            #maybe include a crouch-jump thing
            pass
        if(control.get_d()):
            didimove=a_block.move_xpos(-1,control)
            platformblock.move_xpos(-1,control)
            pb1.move_xpos(-1,control)
            if(didimove):
                a_block.changecolor()
        didblockmove=a_block.move_ypos(control.getvert(),window_height)#gravity does magic
        # if(pygame.sprite.collide_rect(a_block,platformblock)):
        if(not didblockmove and a_block.height+a_block.rect.y==window_height):
            control.setvert(0)
        control.setvert(control.getvert()+gravity)
        clock.tick(frames_per_sec)
        window.fill( [70,40,80])
        block_group.draw(window)
        pygame.display.update()
        print(control.MainSpeed)
    pygame.quit()