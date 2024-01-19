
import mouse
import time

import images
from base_functions import move_and_clic

class Pers():
    """Класс персонажа"""

    def __init__(self, name, icon_name):
        self.name = name
        self.icon_name = icon_name

    def select_pers(self):
        "функция выбора перса"

        xy_tmp = images.find_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
        elif xy_tmp == None:
            time.sleep(3)
            xy_tmp = images.find_coordinates('images/' + self.icon_name)
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
        else:
            time.sleep(3)
            xy_tmp = images.find_coordinates('images/' + self.icon_name)
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            mouse.click('left')
            mouse.click('left')
            move_and_clic(1200, 500)
        time.sleep(11)

class Item():
    """класс игрового ресурса"""
    def __init__(self, name, icon_name):
        "свойства игрового ресурса"
        self.name = name
        self.icon_name = icon_name

    def click(self):
        "функция нажатия на итем"
        xy_tmp = images.find_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 4, y + 4)
        else:
            move_and_clic(1200, 500)
        time.sleep(0.5)

class Take_res():
    def take20(self):
        "метод взятия со склада легиона 20 шт"
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

        def take40(self):
            "метод взятия со склада легиона 40 шт"
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

        def take60(self):
            "метод взятия со склада легиона 40 шт"
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

        def take240(self):
            "метод взятия со склада легиона 240 шт"
            xy_tmp = images.prinat_btn()
            if xy_tmp != None:
                x, y = xy_tmp[0], xy_tmp[1]
                print(x, y)
                # нажать на цифру 2
                move_and_clic(x + 17, y - 61)
                # нажать на цифру 4
                move_and_clic(x - 15, y - 85)
                # нажать на цифру 0
                move_and_clic(x + 86, y - 114)
                # нажать кнопку "принять"
                move_and_clic(x + 11, y + 7)
            else:
                move_and_clic(1200, 500)




# зкземпляры класса Pers
Pers1 = Pers('pers1', "SpielSucht.png")
Pers2 = Pers('pers2', "DeadPonyClub.png")
Pers3 = Pers('pers3', "HungaMunga.png")
Pers4 = Pers('pers4', "Rebyata.png")
Pers5 = Pers('pers5', "KillClericFirst.png")
Pers6 = Pers('pers6', "Huanito.png")
Pers7 = Pers('pers7', "Huanita.png")
Pers8 = Pers('pers8', "spbscale.png")

# # экземпляры класса Item
jelly = Item('jelly', 'jelly.png')
ferera = Item('ferera', 'ferera.png')
ferera_icon = Item('ferera_icon', "")
ferilla = Item('ferilla', "ferilla.png")
grifon = Item('grifon', "grifonia.png")
anis = Item('anis', "anis.png")
sil_stih = Item('sil_stih', "silstih.png")
sil_stih_icon = Item('sil_stih_icon', "")
veton = Item('veton', "veton.png")
okka = Item('okka', "okka.png")
runime = Item('runime', "runime.png")
paporotnik = Item('paporotnik', "paporotnik.png")
silver = Item('silver', "silver.png")
iron_ore = Item('iron_ore', "iron_ore.png")
rukon = Item('rukon', "rukon.png")
diamond = Item('diamond', "diamond.png")
morph = Item('morph', "morph.png")
selected = Item('selected', "selected.png")
sklad_leg_btn = Item('sklad_leg_btn', "sklad_leg_btn.png")
create_all = Item('create_all', "create_all.png")
cross = Item('cross', "cross.png")
menu_btn = Item('menu_btn', "menu_btn.png")

 # = Item('', images)
 # = Item('', images)
 # = Item('', images)
 # = Item('', images)
 # = Item('', images)
 # = Item('', images)








