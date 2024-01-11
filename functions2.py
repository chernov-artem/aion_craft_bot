import pyautogui as pag

import icons
import images
from base_functions import move_and_clic, move_and_right_clic, razbib
from select_pers import *

class Pers():
    """Класс персонажа"""

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def select_pers(self):
        "функция выбора перса"
        xy_tmp = self.icon
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
        elif xy_tmp == None:
            time.sleep(3)
            xy_tmp = self.icon
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
        else:
            time.sleep(3)
            xy_tmp = self.icon
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
            move_and_clic(1200, 500)
        time.sleep(11)





Pers1 = Pers(pers1, images.pers1())
Pers2 = Pers(pers2, images.pers2())
Pers3 = Pers(pers3, images.pers3())
Pers4 = Pers(pers4, images.pers4())
Pers5 = Pers(pers5, images.pers5())
Pers6 = Pers(pers6, images.pers6())
Pers7 = Pers(pers7, images.pers7())
Pers8 = Pers(pers8, images.pers8())



