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
            #self.angle = self.model.angle
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
        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("images/background.png")
        self.world = World(width,height)
        self.ninja = ModelSprite(self.setninja[0][0],model = self.world.ninja)
        self.barrel = ModelSprite('images/item1.png',model = self.world.barrel)
        self.shuriken = ModelSprite('Images/item2.png',model = self.world.shuriken1)
        self.knife = ModelSprite('images/item3.png',model = self.world.knife)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    def update(self,delta):
        self.world.update(delta)
        self.ninja = ModelSprite(self.setninja[self.world.flip][self.world.ninja.pic],model = self.world.ninja)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.ninja.draw()
        self.barrel.draw()
        self.shuriken.draw()
        self.knife.draw()
        arcade.draw_text(str(self.world.score),
                         self.width - 325, self.height - 30,
                         arcade.color.BLACK, 20)


if __name__ == '__main__':
    window =NinninWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()