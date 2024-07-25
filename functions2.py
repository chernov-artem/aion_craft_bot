
import mouse
import time

import pyautogui

import base_functions
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

    def click(self, xdx = 0, xdy = 0, cut = 0):
        "функция нажатия на итем"
        xy_tmp = images.find_coordinates('images/' + self.icon_name, cut)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 6 + xdx, y + 6 + xdy)
        else:
            move_and_clic(1024, 959)
        time.sleep(0.5)

    def click2(self, xdx = 0, xdy = 0):
        "функция нажатия на второй итем по координатам (кликает по вторым найденым координатам объекта)"
        xy_tmp = images.find_second_coordinates('images/' + self.icon_name)
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 6 + xdx, y + 6 + xdy)
        else:
            move_and_clic(1024, 959)
        time.sleep(0.5)

    def take_peace_of_vortex(self):
        "метод взятия эфира из 1 ячейки склада"
        self.click()
        mouse.double_click()

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
    @classmethod
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
    @classmethod
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

    @classmethod
    def put_morph_res_to_main_stock(self, n, big = False):
        """метод позволяет положить все скрафченные ресурсы на главный склад
        желе должно лежать ячейке инвентаря[1] ресурсны складываются начиная с
        ячейки_общ_склада[1][2]
        n - количество складываемых ресурсов
        big - если количество стих камней больше 1000"""
        makros_icon.click()
        sklad_btn.click()

        xy_tmp = images.find_coordinates('images/stock_sign.png')
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)


        for i in range(n):
            base_functions.move_and_clic(x - 67 + i * 45, y + 350)
            mouse.double_click()
        for i in range(n):
            base_functions.move_and_clic(x - 67 + i * 45, y + 470)
            pyautogui.drag(0, -120, 0.6, button='left')
        if big == True:
            base_functions.move_and_clic(x - 157, y + 470)
            pyautogui.drag(0, -165, 0.6, button='left')
        base_functions.move_and_clic(x + 215, y + 3)


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
    def take_vortex(cls):
        "метод взятия эфира со склада. Берет 1 часть эфира. Эфир нужно предварительно разбить на 7 ячеек"
        makros_icon.click()
        time.sleep(1)
        sklad_btn.click()
        # проблема выбора кнопки склада возникает на 7 персе. Возможно его нужно переставить
        vortex40g.take_peace_of_vortex()
        stock_sign.click(215, 3)

    @classmethod
    def take_vortex_pers(cls, pers:object):
        pers.select_pers()
        Instructions.take_vortex()
        Instructions.exit_to_pers_menu()

    @classmethod
    def take_vortex_7pers(cls):
        """метод взятия со склада эфира 7 персами
            эфир нужно предварительно разбить на 7 ячеек

        """
        Instructions.take_vortex_pers(Pers2)
        Instructions.take_vortex_pers(Pers3)
        Instructions.take_vortex_pers(Pers4)
        Instructions.take_vortex_pers(Pers5)
        Instructions.take_vortex_pers(Pers1)
        Instructions.take_vortex_pers(Pers7)
        Instructions.take_vortex_pers(Pers8)


    @classmethod
    def collect_3res(cls, pers: object, n = 1):
        pers.select_pers()
        makros_icon.click()
        time.sleep(1)
        sklad_leg_btn.click()
        Take_res.put_morph_res_to_main_stock(n)
        Instructions.exit_to_pers_menu()
    @classmethod
    def collect_res_all(cls, n = 1):
        Instructions.collect_3res(Pers2, n)
        Instructions.collect_3res(Pers3, n)
        Instructions.collect_3res(Pers4, n)
        Instructions.collect_3res(Pers5, n)
        Instructions.collect_3res(Pers6, n)
        Instructions.collect_3res(Pers7, n)
        Instructions.collect_3res(Pers8, n)



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
        morph.click(684, -45)
        Instructions.exit_to_pers_menu()

    @classmethod
    def craft_pers_pro(cls, pers: object, res: object):
        'метод крафта ресурса выбранным персонажем'

        def sklad_leg():
            'функция открытия склада легиона'
            pyautogui.press('u')
            time.sleep(1.2)
            makros_icon.click()
            time.sleep(1)
            mouse.double_click('left')
            time.sleep(1.5)
            sklad_leg_npc.click(0, 225)
            pyautogui.press('u')

        pers.select_pers()
        #берем эфир со склада лега
        time.sleep(1.9)
        sklad_leg()
        if res == dren_ore:
            vortex50b.click()
            'синий эфир'
        else:
            vortex40g.click()
            'обычный эфир'
        base_functions.take_part()

        if res == neg_almaz or res == neg_ruby or res == neg_sapfire:
            Take_res.take40()
        else:
            Take_res.take20()
        pyautogui.press('Esc', 2, 0.75)
        #крафтим ресурсы
        jelly.click()
        morph.click()
        selected.click()
        res.click()
        create_all.click(10)
        time.sleep(85)
        morph.click(684, -45)
        #кладем ресурсы на склад лега
        pyautogui.press('z', 2, 0.75)
        sklad_leg()
        res.name.click(0, 590, 590)
        mouse.double_click()
        time.sleep(0.9)
        pyautogui.press('Esc', 2, 0.75)
        #выходим на выбор перса
        Instructions.exit_to_pers_menu()


    @classmethod
    def craft_all(cls, res: object):
        'метод крафта одного ресурса всеми 9 персонажами'
        Instructions.craft_pers(Pers1, res)
        Instructions.craft_pers(Pers2, res)
        Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res)
        Instructions.craft_pers(Pers6, res)
        Instructions.craft_pers(Pers7, res)
        Instructions.craft_pers(Pers8, res)
        Instructions.craft_pers(Pers9, res)
        for i in range(10):
            time.sleep(59)
            print('прошло ', i, ' минут')

    @classmethod
    def craft_all_as(cls, res: object):
        'метод крафта одного ресурса всеми 9 персонажами'
        Instructions.craft_pers(Pers01, res)
        Instructions.craft_pers(Pers02, res)
        Instructions.craft_pers(Pers03, res)
        Instructions.craft_pers(Pers04, res)
        Instructions.craft_pers(Pers05, res)
        Instructions.craft_pers(Pers06, res)
        Instructions.craft_pers(Pers07, res)
        Instructions.craft_pers(Pers08, res)
        Instructions.craft_pers(Pers09, res)
        for i in range(10):
            time.sleep(59)
            print('прошло ', i, ' минут')

    @classmethod
    def craft_all_pro_as(cls, res: object):
        'метод крафта одного ресурса всеми 9 персонажами'
        Instructions.craft_pers_pro(Pers01, res)
        Instructions.craft_pers_pro(Pers02, res)
        Instructions.craft_pers_pro(Pers03, res)
        Instructions.craft_pers_pro(Pers04, res)
        Instructions.craft_pers_pro(Pers05, res)
        Instructions.craft_pers_pro(Pers06, res)
        Instructions.craft_pers_pro(Pers07, res)
        Instructions.craft_pers_pro(Pers08, res)
        Instructions.craft_pers_pro(Pers09, res)
        for i in range(10):
            time.sleep(59)
            print('прошло ', i, ' минут')

    @classmethod
    def craft_all_half(cls, res: object, res2: object):
        """
        метод крафта одного ресурса всеми 9 персонажами.
        первый ресурс делается 5 раз, второй четыре раза
        """
        Instructions.craft_pers(Pers1, res)
        Instructions.craft_pers(Pers2, res)
        Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res)
        Instructions.craft_pers(Pers6, res2)
        Instructions.craft_pers(Pers7, res2)
        Instructions.craft_pers(Pers8, res2)
        Instructions.craft_pers(Pers9, res2)
        time.sleep(550)


    @classmethod
    def craft_part(cls, res: object):
        'метод крафта одного ресурса всеми 8 персонажами'
        # Instructions.craft_pers(Pers1, res)
        # Instructions.craft_pers(Pers2, res)
        # Instructions.craft_pers(Pers3, res)
        Instructions.craft_pers(Pers4, res)
        Instructions.craft_pers(Pers5, res)
        Instructions.craft_pers(Pers6, res)
        Instructions.craft_pers(Pers7, res)
        Instructions.craft_pers(Pers8, res)
        Instructions.craft_pers(Pers9, res)
        time.sleep(945)

    @classmethod
    def craft_part_pro_as(cls, res: object):
        'метод крафта одного ресурса всеми 9 персонажами'
        # Instructions.craft_pers_pro(Pers01, res)
        # Instructions.craft_pers_pro(Pers02, res)
        Instructions.craft_pers_pro(Pers03, res)
        Instructions.craft_pers_pro(Pers04, res)
        Instructions.craft_pers_pro(Pers05, res)
        Instructions.craft_pers_pro(Pers06, res)
        Instructions.craft_pers_pro(Pers07, res)
        Instructions.craft_pers_pro(Pers08, res)
        Instructions.craft_pers_pro(Pers09, res)
        for i in range(10):
            time.sleep(59)
            print('прошло ', i, ' минут')

    @classmethod
    def craft_jems(cls):
        'метод крафта одного ресурса всеми 9 персонажами'
        Instructions.craft_pers(Pers1, biruza)
        Instructions.craft_pers(Pers2, turmalin)
        Instructions.craft_pers(Pers3, kelfarat)
        Instructions.craft_pers(Pers4, dren_ore)
        Instructions.craft_pers(Pers5, dren_ore)
        Instructions.craft_pers(Pers6, dren_ore)
        Instructions.craft_pers(Pers7, dren_ore)
        Instructions.craft_pers(Pers8, dren_ore)
        Instructions.craft_pers(Pers9, dren_ore)
        time.sleep(590)

    @classmethod
    def craft_jems_scroll(cls):
        'метод крафта одного ресурса всеми 9 персонажами'
        Instructions.craft_pers_pro(Pers01, neg_almaz)
        Instructions.craft_pers_pro(Pers02, neg_almaz)
        Instructions.craft_pers_pro(Pers03, neg_almaz)
        Instructions.craft_pers_pro(Pers04, neg_almaz)
        Instructions.craft_pers_pro(Pers05, neg_almaz)
        Instructions.craft_pers_pro(Pers06, neg_ruby)
        Instructions.craft_pers_pro(Pers07, neg_ruby)
        Instructions.craft_pers_pro(Pers08, neg_sapfire)
        Instructions.craft_pers_pro(Pers09, neg_sapfire)
        time.sleep(590)

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

    @classmethod
    def buy_water(cls, n, x: int = 0, y: int = 0):
        'метод ускоренной покупки воды у вендора n = 1000 шт'
        time.sleep(2)
        for i in range(n):
            mouse.move(255, 394)
            time.sleep(0.1)
            take_part()
            time.sleep(0.1)
            mouse.move(517, 339)
            time.sleep(0.1)
            mouse.click('left')
            time.sleep(0.1)
            mouse.move(561, 374)
            time.sleep(0.1)
            mouse.click('left')



# зкземпляры класса Pers
Pers1 = Pers('pers1', "pers1.png")
Pers2 = Pers('pers2', "pers2.png")
Pers3 = Pers('pers3', "pers3.png")
Pers4 = Pers('pers4', "pers4.png")
Pers5 = Pers('pers5', "pers5.png")
Pers6 = Pers('pers6', "pers6.png")
Pers7 = Pers('pers7', "pers7.png")
Pers8 = Pers('pers8', "pers8.png")
Pers9 = Pers('pers9', "pers9.png")
Pers01 = Pers('pers01', "pers01.png")
Pers02 = Pers('pers02', "pers02.png")
Pers03 = Pers('pers03', "pers03.png")
Pers04 = Pers('pers04', "pers04.png")
Pers05 = Pers('pers05', "pers05.png")
Pers06 = Pers('pers06', "pers06.png")
Pers07 = Pers('pers07', "pers07.png")
Pers08 = Pers('pers08', "pers08.png")
Pers09 = Pers('pers09', "pers09.png")


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
sklad_btn = Item('stock', 'stock.png')
sklad_leg_btn = Item('sklad_leg_btn', "sklad_leg_btn.png")
sklad_leg_npc = Item('sklad_leg_npc', "sklad_leg_npc.png")
stock_sign = Item('stock_sign', 'stock_sign.png')
create_all = Item('create_all', "create_all.png")
cross = Item('cross', "cross.png")
menu_btn = Item('menu_btn', "menu_btn.png")
sist_menu = Item('sist.menu', 'sist_menu.png')
prinat_btn = Item('prinat_btn', 'prinat_btn.png')
change_pers_button = Item('change_pers_button', 'change_pers_button.png')
blue_grass_icon = Item('blue_grass_icon', 'blue_grass_icon.png')
red_grass_icon = Item('red_grass_icon', 'red_grass_icon.png')
vortex50b = Item("vortex50b", 'vortex50b.png')
vortex40g_icon = Item('vortex40g', 'vortex40g.png')
vortex40g = Item(vortex40g_icon, 'vortex40g.png')
makros_icon = Item('makros_icon', 'makros_icon.png')
top_grass = Item('top_grass', 'top_grass.png')
eode = Item(top_grass, 'eode.png')
gernita = Item(top_grass, 'gernita.png')
kor_fob = Item('kor_fob', 'kor_fob.png')
rafion = Item('rafion', 'rafion.png')
romein = Item('romein', 'romein.png')
pr_stih = Item('pr_stih', 'pr_stih.png')
elit_stih_icon = Item('elit_stih_icon', 'elit_stih_icon.png')
elit_stih = Item(elit_stih_icon, 'elit_stih.png')
grass60 = Item('grass60', 'grass60.png')
besh = Item('besh', 'besh.png')
binan = Item('binan', 'binan.png')
daikon = Item('daikon', 'daikon.png')
tetra = Item('tetra', 'tetra.png')
fenes = Item('fenes', 'fenes.png')
nosfe_icon = Item('nosfe_icon', 'nosfe_icon.png')
nosfe = Item(nosfe_icon, 'nosfe.png')
skin_icon = Item('skin_icon', 'skin_icon.png')
skin = Item(skin_icon, 'skin.png')
dren_ore_icon = Item('dren_ore_icon', 'dren_ore_icon.png')
dren_ore = Item(dren_ore_icon, 'dren_ore.png')
gernita_icon = Item('gernita_icon', 'grass50.png')
biruza = Item('biruza', 'biruza.png')
turmalin = Item('turmalin', 'turmalin.png')
kelfarat = Item('kelfarat', 'kelfarat.png')
neg_almaz_icon = Item('neg_almaz_icon', "neg_almaz_icon.png")
neg_almaz = Item(neg_almaz_icon, "neg_almaz.png")
neg_ruby_icon = Item('neg_ruby_icon', "neg_ruby_icon.png")
neg_ruby = Item(neg_ruby_icon, "neg_ruby.png")
neg_sapfire_icon = Item('neg_sapfire_icon', "neg_sapfire_icon.png")
neg_sapfire = Item(neg_sapfire_icon, "neg_sapfire.png")
riko = Item(top_grass, "riko.png")
foliata = Item(top_grass, "foliata.png")
runas_icon = Item('runas_icon', "runas_icon.png")
runas = Item(runas_icon, "runas.png")
kano_icon = Item('kano_icon', "kano_icon.png")
kano = Item(kano_icon, "kano.png")
jiraka_icon = Item('jiraka_icon', "jiraka_icon.png")
jiraka = Item(jiraka_icon, "Jiraka.png")
menze_icon = Item('menze_icon', "menze_icon.png")
menze = Item(menze_icon, "menze.png")
nalim_icon = Item('nalim_icon', "nalim_icon.png")
nalim = Item(nalim_icon, "nalim.png")
rabeno_icon = Item('rabeno_icon', "rabeno_icon.png")
rabeno = Item(rabeno_icon, "rabeno.png")
serin_icon = Item('serin_icon', "serin_icon.png")
serin = Item(serin_icon, "serin.png")
sibas_icon = Item('sibas_icon', "sibas_icon.png")
sibas = Item(sibas_icon, "sibas.png")
tibaf_icon = Item('tibaf_icon', "tibaf_icon.png")
tibaf = Item(tibaf_icon, "tibaf.png")
gray = Item('', 'gray.png')
botle_icon = Item('botle_icon', 'botle_icon.png')

# fgfd


def drag_res(res: object):
    x, y = images.find_coordinates(f'images/{res.name.icon_name}')
    print('x y = ', x, y)
    move_and_clic(x, y)
    mouse.double_click('left')
    time.sleep(0.9)
    mouse.move(50, 45)
    time.sleep(0.9)
    print(res.name)
    res.name.click()
    pyautogui.dragTo(int(x), int(y), 0.6, button='left')
    mouse.move(35, 41)

time.sleep(2)

# Instructions.craft_jems_scroll()
# Instructions.craft_jems_scroll()
# Instructions.craft_jems_scroll()

# Instructions.craft_part_pro_as(elit_stih)
# Instructions.craft_part_pro_as(elit_stih)

# Instructions.craft_all_pro_as(riko)
# Instructions.craft_all_pro_as(foliata)
# Instructions.craft_all_pro_as(tibaf)
# Instructions.craft_all_pro_as(jiraka)
# Instructions.craft_all_pro_as(serin)
# Instructions.craft_all_pro_as(menze)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(runas)
# Instructions.craft_all_pro_as(runas)
# Instructions.craft_all_pro_as(runas)
# Instructions.craft_all_pro_as(skin)
# Instructions.craft_all_pro_as(skin)
# Instructions.craft_all_pro_as(skin)
# Instructions.craft_all_pro_as(serin)
# Instructions.craft_all_pro_as(menze)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(elit_stih)
# Instructions.craft_all_pro_as(elit_stih)


# botle_icon.click()




# Instructions.buy_water(12)






