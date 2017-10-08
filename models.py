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
            self.vx = -20
        elif self.move == 1:
            self.vx = 20
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
    def __init__(self,world,x,y):
        self.x = -100
        self.y = 1000
        self.posx = [32,568] 
        self.move = [9,10]
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
    def random_location(self):
        '''while(self.sleep<=1000):
            self.sleep+=1'''
        self.rand = randint(0,1)
        if(self.rand == 0):
            self.x = self.posx[randint(0,1)]
        else:
            self.x = -100
        self.y = 1000
        self.speed = self.move[randint(0,1)]
        self.sleep = 0
    def cancel(self):
        self.x  = -100
    def update(self,delta):
        self.y -= self.speed
class World:
    TIMEDELAY = 0.5
    def __init__(self,width,height):
        self.width = width
        self.height  =height
        self.ninja = Ninja(self,568,100)
        self.barrel = Item(self,0,0)
        self.shuriken1 = Item(self,0,0)
        self.barrel2 = Item(self,0,0)
        self.time = 0
        self.check =0
        self.item1 = [self.barrel,self.shuriken1,self.barrel2]
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ninja.direction()
    def update(self,delta):
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
            '''if(self.barrel.y<0):
                self.barrel.random_location()
                if(self.barrel.rand == 0):
                    self.check +=1
            if(self.shuriken1.y <0):
                self.shuriken1.random_location()
                if(self.shuriken1.rand == 0):
                    self.check +=1
            if(self.barrel2.y<0):
                self.barrel2.random_location()
                if(self.barrel2.rand == 0):
                    self.check+=1'''
            print(self.check)
            if(self.check == 2):
                print("in2")
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
            elif(self.check==3):
                print("in3")
                self.barrel.cancel()
                self.barrel2.cancel()
                self.shuriken1.cancel()
            self.check = 0
            self.time = 0    
        