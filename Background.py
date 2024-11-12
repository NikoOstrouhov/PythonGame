import arcade
from Constants import *
class Background():
    def __init__(self, background_image_file):
        # first background image
        self.background_list = arcade.SpriteList()
        #":resources:/images/backgrounds/stars.png"
        self.background_sprite = arcade.Sprite(background_image_file)

        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_sprite.change_y = -SCROLL_SPEED

        self.background_list.append(self.background_sprite)

        # second background image
        self.background_sprite_2 = arcade.Sprite(background_image_file)

        self.background_sprite_2.center_x = SCREEN_WIDTH // 2
        self.background_sprite_2.center_y = (SCREEN_HEIGHT * 2) - 60
        self.background_sprite_2.change_y = -SCROLL_SPEED

        self.background_list.append(self.background_sprite_2)

    def draw(self):

        self.background_list.draw()

    def update(self):

        if self.background_sprite.top <= 0:
            self.background_sprite.center_y = (SCREEN_HEIGHT * 2) + 90

        if self.background_sprite_2.top <= 0:
            self.background_sprite_2.center_y = (SCREEN_HEIGHT * 2) + 90

        self.background_list.update()