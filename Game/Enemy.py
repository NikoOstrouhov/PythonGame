import arcade
import random
import math
from Bullet import *
from Constants import *


class Enemy():
    def __init__(self):
        self.health = None
        self.move_speed = None
        self.sprite = None

        self.place_x = None
        self.place_y = None

    def spawn(self, pos_x,pos_y, ms):
        pass
    def draw(self):
        pass

class Shooter(Enemy):
    def __init__(self):
        super().__init__()
        self.sprite = arcade.Sprite(":resources:/images/space_shooter/Nairan - Bomber - Base.png",1.5)
        self.health = 2
        self.sprite.angle = 180
        self.flag_x_right = True
        self.flag_x_left = True
        self.flag_y_right = True
        self.flag_y_left = True
    def update_move_till_place(self):
        if self.sprite.center_x < self.place_x and self.flag_x_right:
            self.sprite.change_x = self.move_speed
            self.flag_x_left = False
        elif self.sprite.center_x > self.place_x and self.flag_x_left:
            self.sprite.change_x = -self.move_speed
            self.flag_x_right = False
        else:
            self.sprite.change_x = 0
            self.sprite.center_x = self.place_x
        if self.sprite.center_y < self.place_y and self.flag_y_right:
            self.sprite.change_y = self.move_speed
            self.flag_y_left = False
        elif self.sprite.center_y > self.place_y and self.flag_y_left:
            self.sprite.change_y = -self.move_speed
            self.flag_y_right = False
        else:
            self.sprite.change_y = 0
            self.sprite.center_y = self.place_y
        self.sprite.update()

    def update_bullets(self, delta_time, player):
        odds = 150
        adj_odds = int(odds * (1 / 60) / delta_time)
        if random.randrange(adj_odds) == 0:
            bullet = PlasmaGun(ENEMY_BULLET_SPRITE)
            bullet.start_fly(self.sprite.center_x, self.sprite.center_y,0, -3)
            ENEMY_BULLET_LIST.append(bullet)

    def store_place(self,x, y):
        self.place_x = x
        self.place_y = y

    def spawn(self, pos_x, pos_y, ms):
        self.sprite.center_x = pos_x
        self.sprite.center_y = pos_y
        self.move_speed = ms

    def draw(self):
        arcade.draw_sprite(self.sprite)

    def reset_flags(self):
        self.flag_x_right = True
        self.flag_x_left = True
        self.flag_y_right = True
        self.flag_y_left = True

class Aimer(Shooter):
    def __init__(self):
        super().__init__()
        self.sprite = arcade.Sprite(":resources:/images/space_shooter/Nairan - Frigate - Base.png", 1.5)
        self.health = 5
        self.sprite.angle = 180
        self.bullet_speed = 7

    def ready_to_fight(self):
        if self.place_x == self.sprite.center_x and self.place_y == self.sprite.center_y:
            return True
        else:
            return False
    def update_bullets(self, delta_time, player):
        if self.ready_to_fight():
            dest_x = player.sprite.center_x
            dest_y = player.sprite.center_y

            x_diff = dest_x - self.sprite.center_x
            y_diff = dest_y - self.sprite.center_y
            angle = -math.atan2(y_diff, x_diff) + 3.14 / 2
            self.sprite.angle = math.degrees(angle)

            odds = 80
            adj_odds = int(odds * (1 / 60) / delta_time)
            if random.randrange(adj_odds) == 0:
                bullet = PlasmaGun(ENEMY_BULLET_SPRITE)
                bullet.sprite.angle = math.degrees(angle)
                bullet_change_x = math.sin(angle) * self.bullet_speed
                bullet_change_y = math.cos(angle) * self.bullet_speed
                bullet.start_fly(self.sprite.center_x, self.sprite.center_y,bullet_change_x, bullet_change_y)
                ENEMY_BULLET_LIST.append(bullet)

class Boss(Shooter):
    def __init__(self):
        super().__init__()
        self.sprite = arcade.Sprite(":resources:/images/space_shooter/Nairan - Torpedo Ship - Base.png", 3.5)
        self.health = 30
        self.sprite.angle = 180
        self.bullet_speed = 7

    def ready_to_fight(self):
        if self.place_x == self.sprite.center_x and self.place_y == self.sprite.center_y:
            return True
        else:
            return False
    def update_bullets(self, delta_time, player):
        if self.ready_to_fight():
            dest_x = player.sprite.center_x
            dest_y = player.sprite.center_y

            x_diff = dest_x - self.sprite.center_x
            y_diff = dest_y - self.sprite.center_y
            angle = -math.atan2(y_diff, x_diff) + 3.14 / 2
            '''self.sprite.angle = math.degrees(angle)'''

            odds = 85
            adj_odds = int(odds * (1 / 60) / delta_time)
            if random.randrange(adj_odds) == 0:
                bullet = PlasmaGun(ENEMY_BULLET_SPRITE)
                bullet.sprite.angle = math.degrees(angle)
                bullet_change_x = math.sin(angle) * self.bullet_speed
                bullet_change_y = math.cos(angle) * self.bullet_speed
                bullet.start_fly(self.sprite.center_x + 100, self.sprite.center_y,bullet_change_x, bullet_change_y)
                ENEMY_BULLET_LIST.append(bullet)

                bullet = PlasmaGun(ENEMY_BULLET_SPRITE)
                bullet.sprite.angle = math.degrees(angle)
                bullet_change_x = math.sin(angle) * self.bullet_speed
                bullet_change_y = math.cos(angle) * self.bullet_speed
                bullet.start_fly(self.sprite.center_x - 100, self.sprite.center_y, bullet_change_x, bullet_change_y)
                ENEMY_BULLET_LIST.append(bullet)

                bullet = PlasmaGun(ENEMY_BULLET_SPRITE)
                bullet.sprite.angle = math.degrees(angle)
                bullet_change_x = math.sin(angle) * self.bullet_speed * 2
                bullet_change_y = math.cos(angle) * self.bullet_speed * 2
                bullet.start_fly(self.sprite.center_x, self.sprite.center_y, bullet_change_x, bullet_change_y)
                ENEMY_BULLET_LIST.append(bullet)