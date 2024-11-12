import arcade

from Constants import SCREEN_HEIGHT, SCREEN_WIDTH


class PlasmaGun():

    def __init__(self, sprite_image):

        self.sprite = arcade.Sprite(sprite_image,0.5)
        self.sprite.center_x = None
        self.sprite.center_y = None

    def start_fly(self, ship_top_x, ship_top_y, direction_x, direction_y):
        self.sprite.center_x = ship_top_x
        self.sprite.center_y = ship_top_y
        self.sprite.change_x = direction_x
        self.sprite.change_y = direction_y

    def draw_bullet(self):
        arcade.draw_sprite(self.sprite)

class Lazer():
    def __init__(self, sprite_image):
        self.sprite = arcade.Sprite(sprite_image)
        self.sprite.center_x = None
        self.sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite.scale_x = 1
        self.sprite.scale_y = 100
    def start_fly(self, ship_top_x, ship_top_y):
        '''self.sprite.center_x = ship_top_x
        self.sprite.center_y = ship_top_y'''
        self.sprite.center_x = ship_top_x
        self.sprite.bottom = ship_top_y + 20
    def draw_bullet(self):
        arcade.draw_sprite(self.sprite)