import arcade 
from models import World
from random import randint
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
    def draw(self):
        self.sync_with_model()
        super().draw()

class NinninWindow(arcade.Window):
    SLEEP = 0.5
    def __init__(self,width,height):
        super().__init__(width,height)
        self.background = None
        self.wait_time = 0
        self.rand = 0
        self.setninja1 = ['images/char1.png','images/char2.png','images/char3.png','images/char4.png','images/char5.png','images/char6.png']
        self.setninja2 = ['images/char1flip.png','images/char2flip.png','images/char3flip.png','images/char4flip.png','images/char5flip.png','images/char6flip.png']
        self.setninja = [self.setninja1,self.setninja2]
        self.setsheild = ['images/sheild.png','images/sheildflip.png']
        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("images/background.png")
        self.world = World(width,height)
        self.ninja = ModelSprite(self.setninja[0][0],model = self.world.ninja)
        self.sheild = ModelSprite(self.setsheild[0],model = self.world.sheild)
        self.gensheild = ModelSprite('images/item4.png',model = self.world.gensheild)
        self.barrel = ModelSprite('images/item1.png',model = self.world.barrel)
        self.barrel2 = ModelSprite('images/item1.png',model = self.world.barrel2)
        self.shuriken = ModelSprite('Images/item2.png',model = self.world.shuriken1)
        self.knife = ModelSprite('images/item3.png',model = self.world.knife)
        self.textscore = self.ReadScore()
    def setup(self):
        self.world = World(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.ninja = ModelSprite(self.setninja[0][0],model = self.world.ninja)
        self.sheild = ModelSprite(self.setsheild[0],model = self.world.sheild)
        self.gensheild = ModelSprite('images/item4.png',model = self.world.gensheild)
        self.barrel = ModelSprite('images/item1.png',model = self.world.barrel)
        self.barrel2 = ModelSprite('images/item1.png',model = self.world.barrel2)
        self.shuriken = ModelSprite('Images/item2.png',model = self.world.shuriken1)
        self.knife = ModelSprite('images/item3.png',model = self.world.knife)
        self.textscore = self.ReadScore()    
    def ReadScore(self):
        file = open("highscore.txt","r")
        return file.read()
    def WriteScore(self):
        file = open("highscore.txt","w")
        file.write(str(self.world.score))
        file.close()
    def on_key_press(self, key, key_modifiers):
        if(self.world.ninja.status == 1):
            self.world.on_key_press(key, key_modifiers)
        elif(self.world.ninja.status == 0):
            self.setup()
    def update(self,delta):
        if(self.world.ninja.status == 1):
            self.world.update(delta)
            self.ninja = ModelSprite(self.setninja[self.world.flip][self.world.ninja.pic],model = self.world.ninja)
            self.sheild = ModelSprite(self.setsheild[self.world.flip],model = self.world.sheild)
            self.textscore = self.ReadScore()
            if(self.world.score>int(self.textscore)):
                self.WriteScore()
    def drawgameplay(self):
        self.ninja.draw()
        self.sheild.draw()
        self.gensheild.draw()
        self.barrel.draw()
        self.shuriken.draw()
        self.knife.draw()
        self.barrel2.draw()
        arcade.draw_text(str(self.world.score),self.width - 330, self.height - 80,arcade.color.BLUE, 20)
        arcade.draw_text(str("HighScore: "+self.textscore),self.width - 400, self.height - 30,arcade.color.BLUE, 30)
    def drawgameover(self):
        arcade.draw_text(str("HighScore: "+self.textscore),self.width - 400, self.height - 500,arcade.color.BLUE, 30)
        arcade.draw_text(str("YourScore: "+str(self.world.score)),self.width - 350, self.height -550,arcade.color.BLUE, 20)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        if(self.world.ninja.status == 1):
            self.drawgameplay()
        elif(self.world.ninja.status == 0):
            self.drawgameover()
        


if __name__ == '__main__':
    window =NinninWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()