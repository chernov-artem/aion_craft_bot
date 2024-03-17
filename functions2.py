
import mouse
import time

import images
from base_functions import move_and_clic, move_and_double_clic, take_part

class Pers():
    """Класс персонажа"""

    def __init__(self, name, icon_name):
        self.name = name
        self.icon_name = icon_name

    def select_pers(self):
        "функция выбора перса"

        print('Выбрали ', self.name)
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

    def select_tmp(self):
        "функция выбора перса"

        print('Выбрали ', self.name)
        xy_tmp = images.find_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24, y + 8)
            # mouse.click('left')
        time.sleep(2)

class Item():
    """класс игрового ресурса"""
    def __init__(self, name, icon_name):
        "свойства игрового ресурса"
        self.name = name
        self.icon_name = icon_name

    def click(self, xdx = 0, xdy = 0):
        "функция нажатия на итем"
        xy_tmp = images.find_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 6 + xdx, y + 6 + xdy)
        else:
            move_and_clic(1200, 500)
        time.sleep(0.5)

    def take_res(self):
        "метод взятия 120 шт ресурса"
        self.click()
        take_part()
        Take_res.take120()

    def take_res_shift(self):
        "метод для взятия 140 эфира со сдвигом. Второй эфир должен быть справа от первого"
        self.click(60, 15)
        take_part()
        Take_res.take140()

    def double_shift(self):
        'метод для взятия со склада 3 ресурсов(должны лежать в одну линиию)'
        xy_tmp = images.find_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            move_and_double_clic(x, y)
            move_and_double_clic(x + 60, y + 15)
            move_and_double_clic(x + 120, y + 15)
        else:
            move_and_clic(1200, 500)
        time.sleep(0.5)





class Take_res():
    """Класс для взятия со склада нужного количества ресурсов
    в каждом методе поиск абсолютных координат осуществляется только один раз, далее
    используются относительные координаты"""
    @classmethod
    def take20(cls):
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

    @classmethod
    def take40(cls):
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


    @classmethod
    def take60(cls):
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

    def take120(cls):
        "метод взятия со склада легиона 120 шт"
        xy_tmp = images.prinat_btn()
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            # нажать на цифру 1
            move_and_clic(x - 12, y - 57)
            # нажать на цифру 2
            move_and_clic(x + 17, y - 61)
            # нажать на цифру 0
            move_and_clic(x + 86, y - 114)
            # нажать кнопку "принять"
            move_and_clic(x + 11, y + 7)
        else:
            move_and_clic(1200, 500)

    def take140(cls):
        "метод взятия со склада легиона 140 шт"
        xy_tmp = images.prinat_btn()
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            # нажать на цифру 1
            move_and_clic(x - 12, y - 57)
            # нажать на цифру 4
            move_and_clic(x - 12, y - 85)
            # нажать на цифру 0
            move_and_clic(x + 86, y - 114)
            # нажать кнопку "принять"
            move_and_clic(x + 11, y + 7)
        else:
            move_and_clic(1200, 500)


class Instructions():
    """класс инструкций"""
    @classmethod
    def exit_to_pers_menu(cls):
        "функция выхода в меню выбора перса"
        menu_btn.click()
        sist_menu.click()
        change_pers_button.click()
        time.sleep(15)


    @classmethod
    def sklad(cls, name):
        'функция работы со складом'
        Item.name.click()

    @classmethod
    def craft(cls):
        'метод крафта'
        pass

    @classmethod
    def take_vortex(cls):
        "метод взятия эфира со склада. По дефолту берет 120 зел и 140 бел эфира"
        makros_icon.click()
        sklad_leg_btn.click()
        vortex40g.take_res()
        vortex40g.take_res_shift()

    @classmethod
    def take_vortex_pers(cls, pers:object):
        pers.select_pers()
        Instructions.take_vortex()
        cross.click()
        Instructions.exit_to_pers_menu()

    @classmethod
    def take_vortex_6pers(cls):
        """метод взятия со склада эфира 6 персами
           берет 120 зел и 140 белого эфира
           для 8 персов нужно 960 зел эфира и 1120 белого
        """
        Instructions.take_vortex_pers(Pers3)
        Instructions.take_vortex_pers(Pers4)
        Instructions.take_vortex_pers(Pers5)
        Instructions.take_vortex_pers(Pers6)
        Instructions.take_vortex_pers(Pers7)
        Instructions.take_vortex_pers(Pers8)


    @classmethod
    def collect_3res(cls, pers: object):
        pers.select_pers()
        makros_icon.click()
        sklad_leg_btn.click()
        grass60.double_shift()
        grass60.double_shift()
        Instructions.exit_to_pers_menu()
    @classmethod
    def collect_3res_all(cls):
        # Instructions.collect_3res(Pers2)
        Instructions.collect_3res(Pers3)
        Instructions.collect_3res(Pers4)
        Instructions.collect_3res(Pers5)
        Instructions.collect_3res(Pers6)
        Instructions.collect_3res(Pers7)
        Instructions.collect_3res(Pers8)



    @classmethod
    def craft_pers(cls, pers: object, res: object):
        'метод крафта ресурса выбранным персонажем'
        pers.select_pers()
        jelly.click()
        morph.click()
        selected.click()
        res.click()
        create_all.click(10)
        time.sleep(85)
        cross.click()
        Instructions.exit_to_pers_menu()

    @classmethod
    def craft_all(cls, res: object):
        'метод крафта одного ресурса всеми 8 персонажами'
        Instructions.craft_pers(Pers1, res)
        Instructions.craft_pers(Pers2, res)
        Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res)
        Instructions.craft_pers(Pers6, res)
        Instructions.craft_pers(Pers7, res)
        Instructions.craft_pers(Pers8, res)
        time.sleep(635)

    @classmethod
    def craft_all_half(cls, res: object, res2: object):
        'метод крафта одного ресурса всеми 8 персонажами'
        Instructions.craft_pers(Pers1, res)
        Instructions.craft_pers(Pers2, res)
        Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res2)
        Instructions.craft_pers(Pers6, res2)
        Instructions.craft_pers(Pers7, res2)
        Instructions.craft_pers(Pers8, res2)
        time.sleep(635)

    @classmethod
    def craft_part(cls, res: object):
        'метод крафта одного ресурса всеми 8 персонажами'
        # Instructions.craft_pers(Pers1, res)
        # Instructions.craft_pers(Pers2, res)
        Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res)
        Instructions.craft_pers(Pers6, res)
        Instructions.craft_pers(Pers7, res)
        Instructions.craft_pers(Pers8, res)
        time.sleep(830)

    @classmethod
    def fiol_ban(cls):
        """метод крафта ресурсов для фиол банок 1 итерации
         960 зел эфира и 640 белого эфира"""
        Instructions.craft_all_half(eode, gernita)
        Instructions.craft_all_half(eode, gernita)
        Instructions.craft_all(elit_stih)

    @classmethod
    def food_pack(cls):
        """метод крафтит ресурсы на 3 вида еды и 1 вид коктейлей
           требуется 1280 бел эф и 960 зел эф"""
        Instructions.craft_all(eode)
        Instructions.craft_all(gernita)
        Instructions.craft_all(gernita)
        Instructions.craft_all(kor_fob)
        Instructions.craft_all(romein)
        Instructions.craft_all(fenes)
        Instructions.craft_all(daikon)
        Instructions.craft_all(tetra)
        Instructions.craft_all(rafion)
        Instructions.craft_all(besh)
        Instructions.craft_all(binan)
        Instructions.craft_all(eode)
        Instructions.craft_all(gernita)
        Instructions.craft_all(gernita)
        time.sleep(20)
        Pers7.select_pers()

    @classmethod
    def phis_food(cls):
        "метод для крафта ресурсов для физиков. Требует 320 б.эф/160 з.эф"
        Instructions.craft_all(gernita)
        Instructions.craft_all(tetra)
        Instructions.craft_all(rafion)

    @classmethod
    def mag_food(cls):
        "метод для крафта ресурсов для магов. Требует 320 б.эф/160 з.эф"
        Instructions.craft_all(eode)
        Instructions.craft_all(fenes)
        Instructions.craft_all(daikon)

    @classmethod
    def mix_food(cls):
        "метод крафтит 1/2 на физ и 1/2 на маг. Требует 320 б.эф/160 з.эф"
        Instructions.craft_all_half(gernita, eode)
        Instructions.craft_all_half(tetra, fenes)
        Instructions.craft_all_half(rafion, daikon)

    @classmethod
    def chant_food(cls):
        "метод для крафта ресурсов для чантов. Требует 320 б.эф/160 з.эф"
        Instructions.craft_all(gernita)
        Instructions.craft_all(kor_fob)
        Instructions.craft_all(romein)

    @classmethod
    def cocktail(cls):
        'метот крафтит ресы для коктейлей. тр 320 бел эф'
        Instructions.craft_all(besh)
        Instructions.craft_all(binan)













""" сценарии крафта:
1 крафт для жар кор фоб: 1 кор фоб, 1 св гернита 1 ромейн. Полтора часа на 960 еды 
2 крафт для драконик еды: 1 рафион, 1 св эоде 1 час на 960 еды
3 крафт для фереры: 30 мин для 960 еды
4. 


"""







# зкземпляры класса Pers
Pers1 = Pers('pers1', "pers1.png")
Pers2 = Pers('pers2', "pers2.png")
Pers3 = Pers('pers3', "pers3.png")
Pers4 = Pers('pers4', "pers4.png")
Pers5 = Pers('pers5', "pers5.png")
Pers6 = Pers('pers6', "pers6.png")
Pers7 = Pers('pers7', "pers7.png")
Pers8 = Pers('pers8', "pers8.png")

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
sist_menu = Item('sist.menu', 'sist_menu.png')
prinat_btn = Item('prinat_btn', 'prinat_btn.png')
change_pers_button = Item('change_pers_button', 'change_pers_button.png')
blue_grass_icon = Item('blue_grass_icon', 'blue_grass_icon.png')
red_grass_icon = Item('red_grass_icon', 'red_grass_icon.png')
vortex40g = Item('vortex40g', 'vortex40g.png')
makros_icon = Item('makros_icon', 'makros_icon.png')
eode = Item('eode', 'eode.png')
gernita = Item('gernita', 'gernita.png')
kor_fob = Item('kor_fob', 'kor_fob.png')
rafion = Item('rafion', 'rafion.png')
romein = Item('romein', 'romein.png')
pr_stih = Item('pr_stih', 'pr_stih.png')
elit_stih = Item('elit_stih', 'elit_stih.png')
grass60 = Item('grass60', 'grass60.png')
besh = Item('besh', 'besh.png')
binan = Item('binan', 'binan.png')
daikon = Item('daikon', 'daikon.png')
tetra = Item('tetra', 'tetra.png')
fenes = Item('fenes', 'fenes.png')
nosfe = Item('nosfe', 'nosfe.png')
skin = Item('skin', 'skin.png')

time.sleep(2)

Instructions.craft_all(pr_stih)
Instructions.craft_all(pr_stih)


# 1280 / 1120









# Instructions.fiol_ban_x3()
# Instructions.craft_all(romein)
# Instructions.craft_all(besh)
# Instructions.craft_all(binan)


# Instructions.collect_3res_all()
# Instructions.take_vortex_6pers()





