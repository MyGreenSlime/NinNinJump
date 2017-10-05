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
            self.vx = -16
        elif self.move == 1:
            self.vx = 16
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
        self.rand = randint(0,2)
        self.pos = [568,32]
        self.x = -100
        self.y = 1000
        self.speed = [7,10]
        self.move = self.speed[randint(0,1)]
    def random_location(self):
        self.rand = randint(0,2)
        if self.rand ==0:
            self.x = self.pos[randint(0,1)]
        else:
            self.x =-100
        self.y = 1000
        self.move = self.speed[randint(0,1)]
    def update(self,delta):
        self.y-=self.move
class World:
    def __init__(self,width,height):
        self.width = width
        self.height  =height
        self.ninja = Ninja(self,568,100)
        self.barrel = Item(self,0,0)
        self.shuriken1 = Item(self,0,0)
        self.barrel2 = Item(self,0,0)
        self.shuriken2 = Item(self,0,0)
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ninja.direction()
    def update(self,delta):
        self.ninja.update(delta)    
        self.barrel.update(delta)
        self.shuriken1.update(delta)
        self.barrel2.update(delta)  
        self.shuriken2.update(delta)
        if(self.barrel.y<0):
            self.barrel.random_location()
        if(self.shuriken1.y <0):
            self.shuriken1.random_location()
        if(self.barrel2.y<0):
            self.barrel2.random_location()
        if(self.shuriken2.y <0):
            self.shuriken2.random_location()    
        