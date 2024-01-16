
import mouse
import time

import images
from base_functions import move_and_clic

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
        # time.sleep(11)

class Item():
    """класс игрового ресурса"""
    def __init__(self, name, icon):
        "свойства игрового ресурса"
        self.name = name
        self.icon = icon

    def click(self):
        "функция нажатия на итем"
        xy_tmp = self.icon
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 4, y + 4)
        else:
            move_and_clic(1200, 500)
        time.sleep(0.5)

class Take_res():
    def take20():
        "функция взятия со склада легиона 20 шт"
        xy_tmp = images.prinat_btn()
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            # нажать на цифру 2
            move_and_clic(x + 17, y - 61)
            # нажать на цифру 0
            move_and_clic(x + 86, y - 114)
            # нажать кнопку "принять"
            move_and_clic(x + 11, y + 7)
        else:
            move_and_clic(1200, 500)

        def take40():
            "функция взятия со склада легиона 20 шт"
            xy_tmp = images.prinat_btn()
            if xy_tmp != None:
                x, y = xy_tmp[0], xy_tmp[1]
                print(x, y)
                # нажать на цифру 4
                move_and_clic(x - 15, y - 85)
                # нажать на цифру 0
                move_and_clic(x + 86, y - 114)
                # нажать кнопку "принять"
                move_and_clic(x + 11, y + 7)
            else:
                move_and_clic(1200, 500)

        def take60():
            "функция взятия со склада легиона 20 шт"
            xy_tmp = images.prinat_btn()
            if xy_tmp != None:
                x, y = xy_tmp[0], xy_tmp[1]
                print(x, y)
                # нажать на цифру 6
                move_and_clic(x + 45, y - 88)
                # нажать на цифру 0
                move_and_clic(x + 86, y - 114)
                # нажать кнопку "принять"
                move_and_clic(x + 11, y + 7)
            else:
                move_and_clic(1200, 500)




# зкземпляры класса Pers
Pers1 = Pers('pers1', images.pers1())
Pers2 = Pers('pers2', images.pers2())
Pers3 = Pers('pers3', images.pers3())
Pers4 = Pers('pers4', images.pers4())
Pers5 = Pers('pers5', images.pers5())
Pers6 = Pers('pers6', images.pers6())
Pers7 = Pers('pers7', images.pers7())
Pers8 = Pers('pers8', images.pers8())

# экземпляры класса Item
jelly = Item('jelly', images.jelly())
ferera = Item('ferera', images.ferera())
ferera_icon = Item('ferera_icon', images.ferera_icon())
ferilla = Item('ferilla', images.ferilla())
grifon = Item('grifon', images.grifon())
anis = Item('anis', images.anis())
sil_stih = Item('sil_stih', images.sil_stih())
sil_stih_icon = Item('sil_stih_icon', images.sil_stih_icon())
veton = Item('veton', images.veton())
okka = Item('okka', images.okka())
runime = Item('runime', images.runime())
paporotnik = Item('paporotnik', images.paporotnik())
silver = Item('silver', images.silver())
iron_ore = Item('iron_ore', images.iron_ore())
rukon = Item('rukon', images.rukon())
diamond = Item('diamond', images.diamond())
morph = Item('morph', images.morph())
selected = Item('selected', images.selected())
sklad_leg_btn = Item('sklad_leg_btn', images.sklad_leg_btn())
create_all = Item('create_all', images.create_all())
cross = Item('cross', images.cross())
menu_btn = Item('menu_btn', images.menu_btn())
 = Item('', images)
 = Item('', images)
 = Item('', images)
 = Item('', images)
 = Item('', images)
 = Item('', images)








