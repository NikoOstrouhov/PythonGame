from Enemy import *

class Level1():

    def __init__(self):
        #self.background_image = Background(background_image_file)
        self.enemy_list = []
        self.flag_step2 = False

    def step1(self):
        enemy_count = 9
        for i in range(enemy_count):
            bot = Shooter()
            self.enemy_list.append(bot)
        pos_x = 100
        pos_y = SCREEN_HEIGHT + 250
        for i in range(0, enemy_count, 2):
            self.enemy_list[i].spawn(pos_x, pos_y, 10)
            self.enemy_list[i].store_place(pos_x,SCREEN_HEIGHT - 50)
            pos_x += 200

        pos_x = -180
        pos_y = SCREEN_HEIGHT - 100
        self.enemy_list[1].spawn(pos_x, pos_y, 15)
        self.enemy_list[1].store_place(abs(pos_x), pos_y)
        pos_x = -380
        self.enemy_list[3].spawn(pos_x, pos_y, 15)
        self.enemy_list[3].store_place(abs(pos_x), pos_y)

        pos_x = SCREEN_WIDTH + 100
        self.enemy_list[5].spawn(pos_x, pos_y, 15)
        self.enemy_list[5].store_place(abs(SCREEN_WIDTH - 230), pos_y)
        pos_x += 200
        self.enemy_list[7].spawn(pos_x, pos_y, 15)
        self.enemy_list[7].store_place(abs(SCREEN_WIDTH - 430), pos_y)

    def step2(self, checker):
        if checker and self.flag_step2 :
            for i in self.enemy_list:
                i.reset_flags()
                i.move_speed = 0.5
            for i in self.enemy_list:
                i.place_x += -40
            self.flag_step2 = False
        elif checker and not self.flag_step2:
            for i in self.enemy_list:
                i.reset_flags()
                i.move_speed = 0.5
            for i in self.enemy_list:
                i.place_x += 40
            self.flag_step2 = True

class Level2():

    def __init__(self):
        #self.background_image = Background(background_image_file)
        self.enemy_list = []

    def step1(self):
        enemy_count = 5
        for i in range(enemy_count):
            bot = Aimer()
            self.enemy_list.append(bot)
        pos_x = 200
        pos_y = SCREEN_HEIGHT + 250
        for i in range(0,enemy_count,2):
            self.enemy_list[i].spawn(pos_x, pos_y, 6)
            self.enemy_list[i].store_place(pos_x,SCREEN_HEIGHT - 50)
            pos_x += 300
        pos_x = 350
        pos_y = SCREEN_HEIGHT + 200
        for i in range(1,enemy_count,2):
            self.enemy_list[i].spawn(pos_x, pos_y, 6)
            self.enemy_list[i].store_place(pos_x,SCREEN_HEIGHT - 150)
            pos_x += 300


class Level3():

    def __init__(self):
        #self.background_image = Background(background_image_file)
        self.enemy_list = []

    def step1(self):
        enemy_count = 3
        for i in range(enemy_count - 1):
            bot = Aimer()
            self.enemy_list.append(bot)
        boss = Boss()
        self.enemy_list.append(boss)
        pos_x = 200
        pos_y = SCREEN_HEIGHT + 100
        self.enemy_list[0].spawn(pos_x, pos_y, 10)
        self.enemy_list[0].store_place(pos_x,SCREEN_HEIGHT / 2 + 100)
        self.enemy_list[1].spawn(SCREEN_WIDTH - 100, pos_y, 10)
        self.enemy_list[1].store_place(SCREEN_WIDTH - 200, SCREEN_HEIGHT / 2 + 100)
        self.enemy_list[2].spawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT, 10)
        self.enemy_list[2].store_place(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150)