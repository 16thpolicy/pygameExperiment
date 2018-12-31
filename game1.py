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
    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def move_position(self,x,y):
        self.rect.x+=x
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
    window = pygame.display.set_mode(window_size,pygame.RESIZABLE|pygame.FULLSCREEN)




    pygame.display.set_caption("Game by Zhao")



    window.fill( [105,255,205])
    

    clock = pygame.time.Clock() #create object to keep track of time
    frames_per_sec = 30



    block_group = pygame.sprite.Group()
    a_block=Block()

    a_block.set_position(window_width/2,window_height/2)
    current_position=a_block.give_position()

    block_group.add(a_block)

    



    running = True
    while(running):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or event.type== pygame.K_ESCAPE):
                running=False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w):
                    print("+w")
                    a_block.move_position(0,-20)
                    a_block.changecolor()
                if(event.key == pygame.K_a):
                    print("+a")
                    a_block.move_position(-20,0)
                    a_block.changecolor()
                if(event.key == pygame.K_s):
                    print("+s")
                    a_block.move_position(0,+20)
                    a_block.changecolor()
                if(event.key == pygame.K_d):
                    print("+d")
                    a_block.move_position(+20,0)
                    a_block.changecolor()
            if(event.type ==pygame.KEYUP):
                if(event.key == pygame.K_w):
                    print("-w")
                if(event.key == pygame.K_a):
                    print("-a")
                if(event.key == pygame.K_s):
                    print("-s")
                if(event.key == pygame.K_d):
                    print("-d")
        clock.tick(frames_per_sec)
        block_group.draw(window)
        pygame.display.update()

    pygame.quit()