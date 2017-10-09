import arcade.key
from random import randint

class Ninja:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.move = 0
        self.vx = 0
    def direction(self):
        if self.move == 0:
            self.vx = -22
        elif self.move == 1:
            self.vx = 22
    def onhit(self,other,hit_sizex,hit_sizey):
        if((abs(self.x - other.x)<=hit_sizex)and(abs(self.y-other.y)<=hit_sizey)):
            return True
        else: 
            False
    def update(self,delta):
        self.x+=self.vx
        if(abs(600-self.x)<=32):
            self.x = 568
            self.vx = 0
            self.move = 0
        if(abs(600-self.x)>=568):
            self.x = 32
            self.vx = 0
            self.move = 1
class Item():
    TIMEDELAY = 0.2
    def __init__(self,world,x,y):
        self.x = -100
        self.y = randint(1200,1220)
        self.posx = [32,568] 
        self.move = [9,10]
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
        self.time= 0
    def random_location(self):
        self.time = 0
        self.rand = randint(0,1)
        if(self.rand == 0):
            self.x = self.posx[randint(0,1)]
        else:
            self.x = -100
        self.y = randint(1200,1220)
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
    def cancel(self):
        self.x  = -100
    def update(self,delta):
        if(self.time<Item.TIMEDELAY):
            self.time+=delta
        else :
            self.y -= self.speed
class World:
    TIMEDELAY = 0.1
    def __init__(self,width,height):
        self.width = width
        self.height  =height
        self.addscore = 1
        self.score = 0
        self.ninja = Ninja(self,568,100)
        self.barrel = Item(self,0,0)
        self.shuriken1 = Item(self,0,0)
        self.barrel2 = Item(self,0,0)
        self.time = 0
        self.check =0#
        self.item1 = [self.barrel,self.shuriken1,self.barrel2]
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ninja.direction()
    def update(self,delta):
        #print(self.addscore)
        self.score += self.addscore
        self.time += delta
        self.ninja.update(delta)    
        self.barrel.update(delta)
        self.shuriken1.update(delta)
        self.barrel2.update(delta)
        if(self.time>World.TIMEDELAY):
            for i in self.item1:
                if(i.y<0):
                    i.random_location()
                    if(i.rand == 0):
                        self.check+=1
                        if(self.check == 2):
                            #print("in2")
                            for i in self.item1:
                                xx =0
                                for k in self.item1:
                                    if(i != k):
                                        if(i.rand == 0 and k.rand == 0):
                                            xx = 1  
                                            i.cancel()
                                            #k.cancel()
                                            break
                                if(xx == 1):
                                    break
            self.check = 0
            self.time = 0  
        for i in self.item1:
            #print("in")
            if(self.ninja.onhit(i,50,80)==True):
                print("hit")
                self.addscore = 0
                break  