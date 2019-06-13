import pygame

class keyandcover():
    def __init__(self):
        self.w_key=False
        self.a_key=False
        self.s_key=False
        self.d_key=False
        self.a_cover=False
        self.d_cover=False
        self.verticalspeed=0
        self.running = True
        #if in air it cannot accelerate
        self.MainSpeed=0 #MAIN OBJECT
        self.horizontal_terminal_velocity=4

    def setvert(self, x):
        self.verticalspeed=x

    def getvert(self):
        return self.verticalspeed

    def get_w(self):
        return self.w_key

    def get_a(self):
        return self.a_key

    def get_s(self):
        return self.s_key
    
    def get_d(self):
        return self.d_key

    def getrunning(self):
        return self.running
    
    def getMainSpeed(self):
        return self.MainSpeed

    def event_(self,event):
        print("event: ",event)
        if(event.type == pygame.QUIT or (event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE)): #ESC exists game
            self.running=False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_w):
                print("+w")
                self.w_key=True
            elif(event.key == pygame.K_a):
                print("+a")
                if(self.d_key):
                    self.d_key=False
                    self.a_cover=True
                self.MainSpeed=0.2
                self.a_key=True
            elif(event.key == pygame.K_s):
                print("+s")
                self.s_key=True
            elif(event.key == pygame.K_d):
                print("+d")
                if(self.a_key):
                    self.a_key=False
                    self.d_cover=True
                self.MainSpeed=0.2
                self.d_key=True
        if(event.type ==pygame.KEYUP):
            if(event.key == pygame.K_w):
                print("-w")
                self.w_key=False
            elif(event.key == pygame.K_a):
                print("-a")
                self.d_cover=False
                if(self.a_cover):
                    self.d_key=True
                    self.MainSpeed=0.2
                self.a_key=False
            elif(event.key == pygame.K_s):
                print("-s")
                self.s_key=False
            elif(event.key == pygame.K_d):
                print("-d")
                self.a_cover=False
                if(self.d_cover):
                    self.a_key=True
                    self.MainSpeed=0.2
                self.d_key=False
    def accelerate(self):
        if(self.get_a() or self.get_d()):
            self.MainSpeed=round(0.1+self.MainSpeed,1)
        if(self.horizontal_terminal_velocity<self.MainSpeed):
            self.MainSpeed=self.horizontal_terminal_velocity