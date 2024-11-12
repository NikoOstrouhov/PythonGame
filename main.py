"""
Game
"""
import arcade
from Constants import *
from View import MenuView

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView(MUSIC_VOLUME)
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()