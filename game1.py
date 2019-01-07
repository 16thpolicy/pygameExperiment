import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color = (0,0,255), width =64, height = 64):
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
    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def move_position(self,x,y,xbound,ybound):#add parameters
        changeinx=self.rect.x
        changeiny=self.rect.y
        if(self.rect.x+x+self.width>xbound):
            self.rect.x=xbound-self.width
        elif(self.rect.x+x<0):
            self.rect.x=0
        else:
            self.rect.x+=x
        if(self.rect.y+y+self.height>ybound):
            self.rect.y=ybound-self.height
        elif(self.rect.y+y<0):
            self.rect.y=0
        else:
            self.rect.y+=y
        if(changeinx!=self.rect.x or changeiny!=self.rect.y):
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

if(__name__ == "__main__"):
    pygame.init()
    window_size = window_width, window_height = 1080,800
    window = pygame.display.set_mode(window_size,pygame.RESIZABLE)

    pygame.display.set_caption("Game by Zhao")

    window.fill( [105,255,205])
    
    clock = pygame.time.Clock() #create object to keep track of time
    frames_per_sec = 100

    block_group = pygame.sprite.Group()
    a_block=Block()

    platformblock=Block([12,3,12],256,32)
    platformblock.set_position(10,window_height-256)

    a_block.set_position(window_width/2-a_block.rect.width/2,window_height/8)

    block_group.add(a_block,platformblock)

    w_key=False
    a_key=False
    s_key=False
    d_key=False
    a_cover=False
    d_cover=False
    gravity=.15 #positive b/c rip and grid is flipped upside down
    verticalspeed=0
    running = True
    while(running):
        for event in pygame.event.get():
            print("event: ",event)
            if(event.type == pygame.QUIT or (event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running=False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w):
                    print("+w")
                    w_key=True
                elif(event.key == pygame.K_a):
                    print("+a")
                    if(d_key):
                        d_key=False
                        a_cover=True
                    a_key=True
                elif(event.key == pygame.K_s):
                    print("+s")
                    s_key=True
                elif(event.key == pygame.K_d):
                    print("+d")
                    if(a_key):
                        a_key=False
                        d_cover=True
                    d_key=True
            if(event.type ==pygame.KEYUP):
                if(event.key == pygame.K_w):
                    print("-w")
                    w_key=False
                elif(event.key == pygame.K_a):
                    print("-a")
                    d_cover=False
                    if(a_cover):
                        d_key=True
                    a_key=False
                elif(event.key == pygame.K_s):
                    print("-s")
                    s_key=False
                elif(event.key == pygame.K_d):
                    print("-d")
                    a_cover=False
                    if(d_cover):
                        a_key=True
                    d_key=False
        onplatform=pygame.sprite.collide_rect(a_block,platformblock) and a_block.rect.y+a_block.height>=platformblock.rect.y and a_block.rect.y+a_block.height<platformblock.rect.y+5
        underplatform=pygame.sprite.collide_rect(a_block,platformblock) and a_block.rect.y<=platformblock.rect.y+platformblock.height and a_block.rect.y>platformblock.rect.y+platformblock.height-20
        if(onplatform):
            a_block.set_position(a_block.rect.x,platformblock.rect.y-a_block.height)
            verticalspeed=0
        elif(underplatform):
            a_block.set_position(a_block.rect.x,platformblock.rect.y+platformblock.height)
            verticalspeed=0
        if(w_key and (a_block.height+a_block.rect.y==window_height or onplatform)):#if w is pressed and is on a platform
            verticalspeed=-10
            didimove=a_block.move_position(0,-1,window_width,window_height)
            if(didimove):
                a_block.changecolor()
        # elif(w_key):
        #     verticalspeed-=10
        #     w_key=False
        if(a_key):
            didimove= a_block.move_position(-1,0,window_width,window_height)
            if(didimove):
                a_block.changecolor()
        if(s_key):#if on a platform
            #duck
            pass
        if(d_key):
            didimove=a_block.move_position(1,0,window_width,window_height)
            if(didimove):
                a_block.changecolor()
        didblockmove=a_block.move_position(0,verticalspeed,window_width,window_height)#gravity does magic
        # if(pygame.sprite.collide_rect(a_block,platformblock)):
        if(not didblockmove and a_block.height+a_block.rect.y==window_height):
            verticalspeed=0
        verticalspeed+=gravity
        clock.tick(frames_per_sec)
        window.fill( [105,255,205])
        block_group.draw(window)
        pygame.display.update()
    pygame.quit()

