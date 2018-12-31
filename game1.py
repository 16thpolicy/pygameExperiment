import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color = (0,0,255), width =64, height = 64):
        super( Block, self ).__init__() #calling initialize constructor
        self.colorlist=list(color)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.colorR=20
        self.colorG=20
        self.colorB=20
        self.width=width
        self.height=height
    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def move_position(self,x,y,xbound,ybound):#add parameters
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
    def give_position(self):
        return [self.rect.x,self.rect.y]
    def changecolor(self):
        if(self.colorlist[0]+self.colorR>255):
            self.colorR=-20
        elif(self.colorlist[0]+self.colorR<0):
            self.colorR=+20
        if(self.colorlist[1]+self.colorG>255):
            self.colorG=-20
        elif(self.colorlist[1]+self.colorG<0):
            self.colorG=+20
        if(self.colorlist[2]+self.colorB>255):
            self.colorB=-20
        elif(self.colorlist[2]+self.colorB<0):
            self.colorB=+20
        self.colorlist[0]+=self.colorR
        self.colorlist[1]+=self.colorG
        self.colorlist[2]+=self.colorB
        self.image.fill(self.colorlist)

if(__name__ == "__main__"):
    pygame.init()

    window_size = window_width, window_height = 640,480
    window = pygame.display.set_mode(window_size,pygame.RESIZABLE)




    pygame.display.set_caption("Game by Zhao")



    window.fill( [105,255,205])
    

    clock = pygame.time.Clock() #create object to keep track of time
    frames_per_sec = 30



    block_group = pygame.sprite.Group()
    a_block=Block()

    a_block.set_position(window_width/2,window_height/2)
    current_position=a_block.give_position()

    block_group.add(a_block)

    

    w_key=False
    a_key=False
    s_key=False
    d_key=False
    w_cover=False
    a_cover=False
    s_cover=False
    d_cover=False

    running = True
    while(running):
        for event in pygame.event.get():
            print("event: ",event)
            if(event.type == pygame.QUIT or (event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running=False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w):
                    print("+w")
                    if(s_key):
                        s_key=False
                        w_cover=True
                    w_key=True
                elif(event.key == pygame.K_a):
                    print("+a")
                    if(d_key):
                        d_key=False
                        a_cover=True
                    a_key=True
                elif(event.key == pygame.K_s):
                    print("+s")
                    if(w_key):
                        w_key=False
                        s_cover=True
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
                    s_cover=False
                    if(w_cover):
                        s_key=True
                    w_key=False
                elif(event.key == pygame.K_a):
                    print("-a")
                    d_cover=False
                    if(a_cover):
                        d_key=True
                    a_key=False
                elif(event.key == pygame.K_s):
                    print("-s")
                    w_cover=False
                    if(s_cover):
                        w_key=True
                    s_key=False
                elif(event.key == pygame.K_d):
                    print("-d")
                    a_cover=False
                    if(d_cover):
                        a_key=True
                    d_key=False    
        if(w_key):
            a_block.move_position(0,-20,window_width,window_height)
            a_block.changecolor()
        if(a_key):
            a_block.move_position(-20,0,window_width,window_height)
            a_block.changecolor()
        if(s_key):
            a_block.move_position(0,+20,window_width,window_height)
            a_block.changecolor()
        if(d_key):
            a_block.move_position(+20,0,window_width,window_height)
            a_block.changecolor()
        clock.tick(frames_per_sec)
        block_group.draw(window)
        pygame.display.update()
    pygame.quit()