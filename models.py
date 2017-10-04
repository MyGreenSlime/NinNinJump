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
        self.pos = [568,32]
        self.x = self.pos[randint(0,1)]
        self.y = 1200
    def random_location(self):
        self.x = self.pos[randint(0,1)]
        self.y = 1200
    def update(self,delta):
        self.y-=5
class World:
    def __init__(self,width,height):
        self.width = width
        self.height  =height
        self.ninja = Ninja(self,568,300)
        self.barrel = Item(self,0,0)
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ninja.direction()
    def update(self,delta):
        self.ninja.update(delta)
        self.barrel.update(delta)

        if(self.barrel.y<0):
            self.barrel.random_location()
    
        