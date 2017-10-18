import arcade.key
from random import randint

class Ninja:
    def __init__(self,world,x,y,angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        self.move = 0
        self.vx = 0
        self.vy =0
        self.pic = 0
        self.speed =22
        self.status = 1
    def direction(self):
        if self.move == 0:
            self.vx = -self.speed
        elif self.move == 1:
            self.vx = self.speed
    def onhit(self,other,hit_sizex,hit_sizey):
        if((abs(self.x - other.x)<=hit_sizex)and(abs(self.y-other.y)<=hit_sizey)):
            return True
        else: 
            False
    def Die(self):
        self.vy =-10
    def update(self,delta):
        self.y+=self.vy
        self.x+=self.vx
        if(self.y<0):
            self.status = 0
        if(abs(400-self.x)<=32):
            self.x = 368
            self.vx = 0
            self.move = 0
        elif(abs(400-self.x)>=368):
            self.x = 32
            self.vx = 0
            self.move = 1
class Sheild():
    TIMEDELAY = 0.2
    def __init__(self,world,x,y,angle):
        self.x = x
        self.y = y
        self.angle = 0        
        self.posx = -100
        self.posy = -100
    def cancel(self):
        self.posx  = -100
    def position(self,x,y):
        self.posx = x
        self.posy = y
    def update(self,delta):
        self.x = self.posx
        self.y = self.posy
class Item():
    def __init__(self,world,x,y,angle):
        self.x = -100
        self.y = randint(1000,1020)
        self.angle = 0        
        self.posx = [32,368] 
        self.move = [10,10]
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
        self.time= 0
    def random_location(self,range1,range2):
        self.time = 0
        self.rand = randint(range1,range2)
        if(self.rand == 0):
            self.x = self.posx[randint(0,1)]
        else:
            self.x = -100
        self.y = randint(1000,1020)
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
    def cancel(self):
        self.x  = -100
    def setspeed(self,A,B):
        self.move = [A,B]
    def update(self,delta):
            self.y -= self.speed
class World:
    TIMECHANGE = 0.075
    def __init__(self,width,height):
        self.width = width
        self.height  =height
        self.addscore = 1
        self.score = 0
        self.ninja = Ninja(self,368,100,0)
        self.sheild = Sheild(self,368,100,0)
        self.barrel = Item(self,0,0,0)
        self.shuriken1 = Item(self,0,0,0)
        self.knife = Item(self,0,0,0)
        self.gensheild = Item(self,0,0,0)
        self.barrel2 = Item(self,0,0,0)
        self.time = 0
        self.timepic = 0
        self.check =0
        self.item1 = [self.barrel,self.shuriken1,self.knife,self.barrel2]
        self.flip = 0
        self.limitscore = 2500
        self.speeditem1 =11
        self.speeditem2 =12
        self.live = 1
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.live != 0:
            self.ninja.direction()
            if(self.ninja.x==32 or self.ninja.x==368):
                self.flip+=1
                self.flip%=2
    def update(self,delta):
        self.score += self.addscore
        self.time += delta
        self.timepic += delta
        self.ninja.update(delta)
        self.gensheild.update(delta)
        if(self.gensheild.y<0):
            self.gensheild.random_location(0,15)
        if(self.live == 2):
            if(self.flip==1):
                self.sheild.position(self.ninja.x+15,self.ninja.y)
            else: 
                self.sheild.position(self.ninja.x-15,self.ninja.y)
        self.sheild.update(delta)
        for i in self.item1:
            i.update(delta)
        if(self.score>=self.limitscore):
            for i in self.item1:
                i.setspeed(self.speeditem1,self.speeditem2)
            self.gensheild.setspeed(self.speeditem1,self.speeditem2)
            self.speeditem1+=2
            self.speeditem2+=2
            self.limitscore+=2500
            self.ninja.speed+=2
        j = 0
        timeset = [0.1,0.4,0.7,1,1.3]
        for i in self.item1:
            if(i.y<0 and (self.time%2 >=timeset[j] and self.time%2<=timeset[j+1]-0.2)):
                i.random_location(0,1)
            j+=1
        if(self.timepic>=World.TIMECHANGE):
            self.ninja.pic+=1
            self.ninja.pic%=6   
            self.timepic = 0   
        for i in self.item1:
            if(self.ninja.onhit(i,50,70)==True):
                self.live-=1
                if(self.live == 1):
                    self.sheild.cancel()
                    i.cancel()
                elif(self.live == 0):
                    if(self.flip == 0):
                        self.ninja.angle = 90
                    else:
                        self.ninja.angle = -90
                    self.ninja.Die()
                    self.addscore =0
                break 
        if(self.ninja.onhit(self.gensheild,50,70)==True):
            self.gensheild.cancel()
            if(self.live<=1):
                self.live+=1