
from pico2d import *
import game_world
import server
import collide


class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image == None:
            Ball.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
         return self.x-8,self.y-8,self.x+8,self.y+8

    def draw(self):
        self.image.draw(self.x, self.y,15,15)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        if self.x<25 or self.x > 1600-25:
            game_world.remove_object(self)

    # def stop(self):
    #     self.fall_speed = 0




