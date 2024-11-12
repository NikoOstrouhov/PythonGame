import arcade
import time
from Constants import *

class Player():
    def __init__(self):

        self.plasma_rate_of_fire = PLASMA_RATE_OF_FIRE

        self.lazer_rate_of_fire = LAZER_RATE_OF_FIRE

        self.health = 3

        self.gun_plasma = True

        self.gun_lazer = False

        self.sprite = arcade.Sprite(PLAYER_SPRITE, PLAYER_CHARACTER_SCALING)

        self.sprite.center_x = SCREEN_WIDTH / 2

        self.sprite.center_y = SCREEN_HEIGHT / 8

    def draw(self):
        arcade.draw_sprite(self.sprite)

    def update(self, player_bullet_list, enemy_list, enemy_bullet_list, last_fire):
        if self.sprite.left <= 0:
            self.sprite.left = 0
        if self.sprite.right >= SCREEN_WIDTH:
            self.sprite.right = SCREEN_WIDTH

        for bullet in player_bullet_list:
            for enemy in enemy_list:
                if arcade.check_for_collision(bullet.sprite, enemy.sprite) and self.gun_plasma:
                    player_bullet_list.remove(bullet)
                    enemy.health -= 1
                    if enemy.health <= 0:
                        enemy_list.remove(enemy)
                if self.gun_lazer:
                    bullet.sprite.center_x = self.sprite.center_x
                    bullet.sprite.bottom = self.sprite.center_y + 20
                if arcade.check_for_collision(bullet.sprite, enemy.sprite) and self.gun_lazer:
                    enemy.health -= 0.25
                    if enemy.health <= 0:
                        enemy_list.remove(enemy)
                if player_bullet_list and time.time() - last_fire > 1.5 and self.gun_lazer:
                    player_bullet_list.remove(bullet)

        for bullet in enemy_bullet_list:
            if arcade.check_for_collision(bullet.sprite, self.sprite):
                enemy_bullet_list.remove(bullet)
                self.health -= 1

        for bullet in player_bullet_list:
            if bullet.sprite.bottom > SCREEN_HEIGHT and not self.gun_lazer:
                player_bullet_list.remove(bullet)

        for bullet in player_bullet_list:
            bullet.sprite.update()