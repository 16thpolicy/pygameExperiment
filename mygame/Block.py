import pygame
from keyandcover import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color = (0,0,255), width =64, height = 64,fraction=0):
        super( Block, self ).__init__() #calling initialize constructor
        self.colorlist=list(color)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.colorR=3
        self.colorG=9
        self.colorB=14
        self.width=width
        self.height=height
        self.fraction=fraction
        #make a bool for airborne
    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def move_ypos(self,y,ybound):#add parameters need it to check from a list of rects for now
        changeiny=self.rect.y
        if(self.rect.y+y+self.height>ybound):
            self.rect.y=ybound-self.height
        elif(self.rect.y+y<0):
            self.rect.y=0
        else:
            self.rect.y+=y
        if(changeiny!=self.rect.y):
            return True
        return False
    def changecolor(self):
        if(self.colorlist[0]+self.colorR>255):
            self.colorR=-3
        elif(self.colorlist[0]+self.colorR<0):
            self.colorR=3
        if(self.colorlist[1]+self.colorG>255):
            self.colorG=-9
        elif(self.colorlist[1]+self.colorG<0):
            self.colorG=9
        if(self.colorlist[2]+self.colorB>255):
            self.colorB=-14
        elif(self.colorlist[2]+self.colorB<0):
            self.colorB=14
        self.colorlist[0]+=self.colorR
        self.colorlist[1]+=self.colorG
        self.colorlist[2]+=self.colorB
        self.image.fill(self.colorlist)
    def move_xpos(self,val,kac): #MOVES the Objects here
        self.rect.x+=(val*kac.getMainSpeed()*self.fraction)
        return self.rect.x