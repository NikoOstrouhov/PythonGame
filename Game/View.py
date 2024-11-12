from typing import List

import arcade
import arcade.gui
import time
from Background import Background
from Player import Player
from Levels import *

class SubMenu(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    """Acts like a fake view/window."""

    def __init__(self, main_view):
        super().__init__(size_hint=(1, 1))

        # Setup frame which will act like the window.
        frame = self.add(arcade.gui.UIAnchorLayout(width=500, height=600, size_hint=None))
        frame.with_padding(all=20)

        # Add a background to the window.
        # Nine patch smoothes the edges.
        frame.with_background(
            texture=arcade.gui.NinePatchTexture(
                left=7,
                right=7,
                bottom=7,
                top=7,
                texture=arcade.load_texture(
                    ":resources:gui_basic_assets/window/dark_blue_gray_panel.png"
                ),
            )
        )
        self.main_view = main_view
        back_button = arcade.gui.UIFlatButton(text="Back", width=250)
        # The type of event listener we used earlier for the button will not work here.
        back_button.on_click = self.on_click_back_button

        title_label = arcade.gui.UILabel(text="Inventory", align="center", font_size=20, multiline=False)
        # Adding some extra space around the title.

        # Load the on-off textures.
        on_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_on.png"
        )
        off_texture = arcade.load_texture(
            ":resources:gui_basic_assets/simple_checkbox/circle_off.png"
        )

        guns_label = arcade.gui.UILabel(text="Guns", align="left", font_size=20, multiline=False)
        # Create the on-off toggle and a label
        toggle_label1 = arcade.gui.UILabel(text="PlasmaGun",font_size=20)
        self.toggle1 = arcade.gui.UITextureToggle(
            on_texture=on_texture, off_texture=off_texture, width=20, height=20
        )
        self.toggle1.value = main_view.player_gun_plasma
        toggle_label2 = arcade.gui.UILabel(text="Lazer",font_size=20)
        self.toggle2 = arcade.gui.UITextureToggle(
            on_texture=on_texture, off_texture=off_texture, width=20, height=20
        )
        self.toggle2.value = main_view.player_gun_lazer

        # Align toggle and label horizontally next to each other
        gun1_group = arcade.gui.UIBoxLayout(vertical=False,space_between=10,align="left")
        gun1_group.add(self.toggle1)
        gun1_group.add(toggle_label1)
        gun2_group = arcade.gui.UIBoxLayout(vertical=False,space_between=10,align="left")
        gun2_group.add(self.toggle2)
        gun2_group.add(toggle_label2)
        toggle_group1 = arcade.gui.UIBoxLayout(vertical=True, space_between=20, align="left")
        toggle_group1.add(gun1_group)
        toggle_group1.add(gun2_group)

        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        widget_layout.add(guns_label)
        widget_layout.add(toggle_group1)

        '''widget_layout.add(back_button)'''

        frame.add(child=title_label, anchor_x="center_x", anchor_y="top")
        frame.add(child=widget_layout, align_y= frame.center_y - 250, align_x = frame.center_x - 350)
        frame.add(child=back_button, anchor_x="center_x", anchor_y="bottom")

        @self.toggle1.event("on_change")
        def on_click_switch_button(event):
            if self.toggle1.value:
                self.toggle2.value = False
            if not self.toggle1.value and not self.toggle2.value:
                self.toggle1.value = True

        @self.toggle2.event("on_change")
        def on_click_switch_button(event):
            if self.toggle2.value:
                self.toggle1.value = False
            if not self.toggle1.value and not self.toggle2.value:
                self.toggle2.value = True

    def on_click_back_button(self, event):
        # Removes the widget from the manager.
        # After this the manager will respond to its events like it previously did.
        self.parent.remove(self)
        self.main_view.player_gun_plasma = self.toggle1.value
        self.main_view.player_gun_lazer = self.toggle2.value

class MainView(arcade.View):
    """This is the class where your normal game would go."""

    def __init__(self, menu_view, menu_playback):
        super().__init__()

        self.player_gun_plasma = True

        self.player_gun_lazer = False

        self.manager = arcade.gui.UIManager()
        level1_button = arcade.gui.UIFlatButton(text="Level 1", width=100)
        level2_button = arcade.gui.UIFlatButton(text="Level 2", width=100)
        level3_button = arcade.gui.UIFlatButton(text="Level 3", width=100)
        shop_button = arcade.gui.UIFlatButton(text="Inventory", width=340)
        back_button = arcade.gui.UIFlatButton(text="Back", width=340)

        self.grid = arcade.gui.UIGridLayout(
            column_count=3, row_count=3, horizontal_spacing=20, vertical_spacing=20
        )
        self.grid.add(level1_button, column=0, row=0)
        self.grid.add(level2_button, column=1, row=0)
        self.grid.add(level3_button, column=2, row=0)
        self.grid.add(shop_button, column=0, row=1, column_span=3)
        self.grid.add(back_button, column=0, row=2, column_span=3)

        # Initialise the button with an on_click event.
        @back_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            self.window.show_view(menu_view)

        @level1_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            game = MyGame(1, menu_view,self)
            game.setup()
            self.window.show_view(game)
            menu_playback.pause()

        @level2_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            game = MyGame(2, menu_view, self)
            game.setup()
            self.window.show_view(game)
            menu_playback.pause()

        @level3_button.event("on_click")
        def on_click_switch_button(event):
            # Passing the main view into menu view as an argument.
            game = MyGame(3, menu_view, self)
            game.setup()
            self.window.show_view(game)
            menu_playback.pause()

        @shop_button.event("on_click")
        def on_click_switch_button(event):
            options_menu = SubMenu(self)
            self.manager.add(options_menu, layer=1)

        # Use the anchor to position the button on the screen.
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid,
        )

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Enable the UIManager when the view is showm.
        self.manager.enable()

    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        background = Background(LEVEL_MENU_BACKGROUND_IMAGE_FILE)
        background.draw()
        # Draw the manager.
        self.manager.draw()



class MenuView(arcade.View):
    """Main menu view class."""

    def __init__(self,music_volume):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.music_volume = music_volume / 100
        self.menu_music = arcade.load_sound(MAIN_MENU_MUSIC_FILE)
        self.menu_playback = arcade.play_sound(self.menu_music, loop = True, volume = self.music_volume)

        name_label = arcade.gui.UILabel(text="Space Shooter", align="center", font_size=35, multiline=False)
        start_game_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        options_button = arcade.gui.UIFlatButton(text="Options", width=200)

        exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)

        self.v_box = arcade.gui.UIBoxLayout(space_between=30)
        self.v_box.add(name_label)
        self.v_box.add(start_game_button)
        self.v_box.add(options_button)
        self.v_box.add(exit_button)

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box,
        )

        self.options_menu = OptionsMenu(self)

        @start_game_button.event("on_click")
        def on_click_resume_button(event):
            # Pass already created view because we are resuming.
            main_view = MainView(self,self.menu_playback)
            self.window.show_view(main_view)

        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()

        @options_button.event("on_click")
        def on_click_options_button(event):
            self.window.show_view(self.options_menu)

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""
        # Enable the UIManager when the view is showm.
        self.manager.enable()

    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        background = Background(MENU_BACKGROUND_IMAGE_FILE)
        background.draw()
        self.manager.draw()


class OptionsMenu(arcade.View):
    """Acts like a fake view/window."""

    def __init__(self, menu_view):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        # Setup frame which will act like the window.

        self.menu = menu_view

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        back_button = arcade.gui.UIFlatButton(text="Back", width=250)

        title_label = arcade.gui.UILabel(text="Settings", align="center", font_size=20, multiline=False)
        # Adding some extra space around the title.
        title_label_space = arcade.gui.UISpace(height=30)

        slider_label_music = arcade.gui.UILabel(text="Music mixer")

        # Configuring the styles is optional.

        self.slider_music = arcade.gui.UISlider(value=MUSIC_VOLUME, width=250)

        widget_layout = arcade.gui.UIBoxLayout(space_between=10)
        widget_layout.add(title_label)
        widget_layout.add(title_label_space)
        widget_layout.add(slider_label_music)
        widget_layout.add(self.slider_music)

        widget_layout.add(back_button)

        self.anchor.add(child=widget_layout, anchor_x="center_x", anchor_y="center_y")

        @back_button.event("on_click")
        def on_click_back_button(event):
            self.window.show_view(menu_view)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        background = Background(SETTINGS_BACKGROUND_IMAGE_FILE)
        background.draw()
        self.manager.draw()
        self.menu.music_volume = self.slider_music.value / 100
        self.menu.menu_playback.volume = self.menu.music_volume

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        """This is run once when we switch to this view"""
        self.manager.enable()

class ResultView(arcade.View):
    """ View to show when game is over """

    def __init__(self,menu_view,main_view,result):
        """ This is run once when we switch to this view """
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        self.music_volume = menu_view.music_volume
        self.result_playback = None
        self.result_music = None
        if result:
            result_text = "VICTORY!"
            game_over_label = arcade.gui.UILabel(text=result_text, align="center", font_size=60, multiline=False)
            self.result_music = arcade.load_sound(VICTORY_MENU_MUSIC_FILE)
        else:
            result_text = "GAME OVER"
            game_over_label = arcade.gui.UILabel(text=result_text, align="center", font_size=60, multiline=False)
            self.result_music = arcade.load_sound(GAME_OVER_MUSIC_FILE)
        label_space = arcade.gui.UISpace(height=50)
        continue_button = arcade.gui.UIFlatButton(text="Continue", width=250)
        back_menu_button = arcade.gui.UIFlatButton(text="Back to Main Menu", width=250)

        widget_layout = arcade.gui.UIBoxLayout(align="Center", space_between=10)
        widget_layout.add(game_over_label)
        widget_layout.add(label_space)
        widget_layout.add(continue_button)
        widget_layout.add(back_menu_button)


        self.anchor.add(child=widget_layout, anchor_x="center_x", anchor_y="center_y")

        @continue_button.event("on_click")
        def on_click_exit_button(event):
            self.window.show_view(main_view)
            menu_view.menu_playback.play()
        @back_menu_button.event("on_click")
        def on_click_options_button(event):
            self.window.show_view(menu_view)
            menu_view.menu_playback.play()
    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.manager.draw()
    def on_hide_view(self):
        self.manager.disable()
        arcade.stop_sound(self.result_playback)
    def on_show_view(self):
        """This is run once when we switch to this view"""
        arcade.set_background_color([0,0,0,0])
        self.result_playback = arcade.play_sound(self.result_music, volume = self.music_volume)
        self.manager.enable()

class MyGame(arcade.View):

    def __init__(self, level_number, menu_view, main_view):

        # Call the parent class and set up the window
        super().__init__()

        self.level_number = level_number

        self.player = None

        self.player_gun_plasma = main_view.player_gun_plasma

        self.player_gun_lazer = main_view.player_gun_lazer

        self.player_bullet_list = None

        self.enemy_list = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False

        self.player_last_fire = None

        self.background = None

        self.level1 = None

        self.level2 = None

        self.level3 = None

        self.physics_engine = None

        self.game_over = ResultView(menu_view, main_view,False)

        self.victory = ResultView(menu_view, main_view,True)

        self.music_volume = menu_view.music_volume

        self.level_playback = None

    def setup(self):
        arcade.set_background_color([0,0,0,0])

        self.player = Player()

        self.player.gun_plasma = self.player_gun_plasma
        self.player.gun_lazer = self.player_gun_lazer

        self.player_bullet_list = []
        if self.level_number == 1:
            self.level1 = Level1()
            self.level1.step1()
            self.background = Background(LEVEL1_BACKGROUND_IMAGE_FILE)
            level1_music = arcade.load_sound(LEVEL1_MUSIC_FILE)
            self.level_playback = arcade.play_sound(level1_music, loop = True, volume = self.music_volume)
        if self.level_number == 2:
            self.level2 = Level2()
            self.level2.step1()
            self.background = Background(LEVEL2_BACKGROUND_IMAGE_FILE)
            level2_music = arcade.load_sound(LEVEL2_MUSIC_FILE)
            self.level_playback = arcade.play_sound(level2_music, loop=True, volume = self.music_volume)
        if self.level_number == 3:
            self.level3 = Level3()
            self.level3.step1()
            self.background = Background(LEVEL3_BACKGROUND_IMAGE_FILE)
            level3_music = arcade.load_sound(LEVEL3_MUSIC_FILE)
            self.level_playback = arcade.play_sound(level3_music, loop=True, volume = self.music_volume)

        self.player_last_fire = time.time()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player.sprite, None)

    def on_draw(self):
        """Render the screen."""

        self.clear()

        self.background.draw()

        if self.level_number == 1:
            for enemy in self.level1.enemy_list:
                enemy.draw()
        if self.level_number == 2:
            for enemy in self.level2.enemy_list:
                enemy.draw()
        if self.level_number == 3:
            for enemy in self.level3.enemy_list:
                enemy.draw()

        self.player.draw()

        for bullets in self.player_bullet_list:
            bullets.draw_bullet()

        for bullet in ENEMY_BULLET_LIST:
            bullet.draw_bullet()

    def update_player_speed(self):
        # Calculate speed based on the keys pressed
        self.player.sprite.change_x = 0
        self.player.sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player.sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()

        if key == arcade.key.SPACE and self.player.gun_plasma:
            if time.time() - self.player_last_fire > self.player.plasma_rate_of_fire / 1.5:
                self.space_pressed = True
                bullet = PlasmaGun(PLAYER_BULLET_SPRITE)
                bullet.start_fly(self.player.sprite.center_x, self.player.sprite.center_y + 40,0, 5)
                self.player_bullet_list.append(bullet)
                self.player_last_fire = time.time()
        if key == arcade.key.SPACE and self.player.gun_lazer:
            if time.time() - self.player_last_fire > self.player.lazer_rate_of_fire:
                self.space_pressed = True
                bullet = Lazer(PLAYER_BULLET_SPRITE)
                bullet.start_fly(self.player.sprite.center_x, self.player.sprite.center_y)
                self.player_bullet_list.append(bullet)
                self.player_last_fire = time.time()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()
        if key == arcade.key.SPACE:
            self.space_pressed = False

    def check_place(self, enemy_list):
        """Check whether the enemies have reached their destination"""
        flag_place = True
        for enemy in enemy_list:
            if not (enemy.place_x == enemy.sprite.center_x and enemy.place_y == enemy.sprite.center_y):
                flag_place = False
        return flag_place

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.physics_engine.update()

        self.background.update()

        if self.player.health <= 0:
            ENEMY_BULLET_LIST.clear()
            self.window.show_view(self.game_over)
            arcade.stop_sound(self.level_playback)
        if self.level_number == 1:
            if not self.level1.enemy_list:
                ENEMY_BULLET_LIST.clear()
                self.window.show_view(self.victory)
                arcade.stop_sound(self.level_playback)
            for enemy in self.level1.enemy_list:
                enemy.update_move_till_place()
            self.player.update(self.player_bullet_list, self.level1.enemy_list,ENEMY_BULLET_LIST,self.player_last_fire)

            if self.level1.enemy_list:
                self.level1.step2(self.check_place(self.level1.enemy_list))

            for enemy in self.level1.enemy_list:
                enemy.update_bullets(delta_time, self.player)

        if self.level_number == 2:
            if not self.level2.enemy_list:
                ENEMY_BULLET_LIST.clear()
                self.window.show_view(self.victory)
                arcade.stop_sound(self.level_playback)
            self.player.update(self.player_bullet_list, self.level2.enemy_list,ENEMY_BULLET_LIST,self.player_last_fire)

            for enemy in self.level2.enemy_list:
                enemy.update_move_till_place()

            for enemy in self.level2.enemy_list:
                enemy.update_bullets(delta_time, self.player)

        if self.level_number == 3:
            if not self.level3.enemy_list:
                ENEMY_BULLET_LIST.clear()
                self.window.show_view(self.victory)
                arcade.stop_sound(self.level_playback)
            self.player.update(self.player_bullet_list, self.level3.enemy_list,ENEMY_BULLET_LIST,self.player_last_fire)

            for enemy in self.level3.enemy_list:
                enemy.update_move_till_place()

            for enemy in self.level3.enemy_list:
                enemy.update_bullets(delta_time, self.player)

        for bullet in ENEMY_BULLET_LIST:
            if bullet.sprite.bottom < 0 or bullet.sprite.bottom > SCREEN_HEIGHT:
                ENEMY_BULLET_LIST.remove(bullet)

        for bullet in ENEMY_BULLET_LIST:
            bullet.sprite.update()

        if self.space_pressed and self.player.gun_plasma:
            if time.time() - self.player_last_fire > self.player.plasma_rate_of_fire:
                bullet = PlasmaGun(PLAYER_BULLET_SPRITE)
                bullet.start_fly(self.player.sprite.center_x, self.player.sprite.center_y + 40, 0,5)
                self.player_bullet_list.append(bullet)
                self.player_last_fire = time.time()
