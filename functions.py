import pyautogui as pag


import time
import mouse

import icons
import images
from base_functions import move_and_clic, move_and_right_clic, razbib
# from select_pers import *


def get_position():
    time.sleep(2)
    current_cursor = mouse.get_position()
    print(current_cursor)


def change_pers():
    "функция нажатия на кнопку смены игрока"
    xy_tmp = images.change_pers()
    x, y = xy_tmp[0], xy_tmp[1]
    move_and_clic(x+35, y+8)

def jelly():
    "функция нажатия на желе"
    xy_tmp = images.jelly()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.5)

def ferera():
    "функция нажатия на фереру"
    xy_tmp = images.ferera()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.4)

def ferilla():
    "функция нажатия на свежую фериллу"
    xy_tmp = images.ferilla()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.4)

def grifon():
    "функция нажатия на свежую грифонию"
    xy_tmp = images.grifon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.4)

def anis():
    "функция нажатия на свежий звездный анис "
    xy_tmp = images.anis()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.41)

def sil_stih():
    "функция нажатия на сильный стихийный камень(белый)"
    xy_tmp = images.sil_stih()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.42)

def veton():
    "функция нажатия на свежий ветон "
    xy_tmp = images.veton()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.43)

def okka():
    "функция нажатия на окку "
    xy_tmp = images.okka()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.44)

def runime():
    "функция нажатия на рунимэ "
    xy_tmp = images.runime()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.45)

def paporotnik():
    "функция нажатия на свежий папоротник "
    xy_tmp = images.paporotnik()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.44)

def silver():
    "функция нажатия на серебряную руду"
    xy_tmp = images.silver()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.43)

def iron_ore():
    "функция нажатия на железную руду"
    xy_tmp = images.iron_ore()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.42)
def rukon():
    "функция нажатия на стебель рюкона"
    xy_tmp = images.rukon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.44)

def diamond():
    "функция нажатия на алмаз "
    xy_tmp = images.diamond()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.44)
def morph():
    "функция нажатия кнопки преобразования"
    xy_tmp = images.morph()
    x, y = xy_tmp[0], xy_tmp[1]
    print(x, y)
    move_and_clic(x+24, y+8)
    time.sleep(0.6)

def selected():
    "функция нажатия ячейки выбранные"
    xy_tmp = images.selected()
    x, y = xy_tmp[0], xy_tmp[1]
    print(x, y)
    move_and_clic(x+11, y+9)
    time.sleep(0.5)

def sklad_leg_btn():
    "функция нажатия на кнопку склада лега"
    xy_tmp = images.sklad_leg_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.45)

def create_all():
    "функция нажатия на кнопку изготовить всё"
    xy_tmp = images.create_all()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.5)

def cross():
    "функция нажатия на кнопку крестика"
    xy_tmp = images.cross()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
        # mouse.click('left')
        # mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(0.53)

def menu_btn():
    "функция нажатия на кнопку меню"
    xy_tmp = images.menu_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
        # mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(0.9)
    xy_tmp = images.sist_menu()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.9)

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
        #нажать кнопку "принять"
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
        #нажать кнопку "принять"
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
        #нажать кнопку "принять"
        move_and_clic(x + 11, y + 7)
    else:
        move_and_clic(1200, 500)

def take240():
    "функция взятия со склада легиона 240 шт"
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
        #нажать кнопку "принять"
        move_and_clic(x + 11, y + 7)
    else:
        move_and_clic(1200, 500)



def exit():
    "функция выхода в меню выбора перса"
    print('выход запущен')
    pag.typewrite('o', 0)
    print('нажал o')
    time.sleep(0.6)
    if images.change_pers() == None:
        menu_btn()
        print('нажал на меню мышкой')
        change_pers()
    else:
        change_pers()
    time.sleep(15)

def sklad_funktions():
    "функция действий на складе"
    # sil_stih_icon()
    # icons.blue_grass_icon()
    # icons.red_grass_icon()
    icons.ferera_icon()
    # vortex40()
    # take60()
def sklad():
    "функция работы со складом легиона"
    pag.typewrite('9', 1)
    time.sleep(0.44)
    pag.typewrite('c', 1)
    sklad_leg_btn()
    # что сделать на складе:
    sklad_funktions()
    time.sleep(0.3)
    sklad_funktions()
    time.sleep(2)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def sklad_take_res():
    "функция получения ресурсов со склада легиона"
    pag.typewrite('9', 1)
    time.sleep(0.44)
    pag.typewrite('c', 1)
    sklad_leg_btn()
    # что сделать на складе:
    sklad_funktions()
    time.sleep(2)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft():
    "функция крафта ресурсов из эфира"
    # pag.typewrite('9', 1)
    # time.sleep(0.44)
    # pag.typewrite('c', 1)
    # sklad_leg_btn()
    # icons.vortex40_icon()
    # take20()
    cross()
    jelly()
    morph()
    selected()
    # ferera()
    # ferilla()
    # grifon()
    # anis()
    sil_stih()
    # veton()
    # paporotnik()
    # diamond()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_pers1():
    "функция крафта ресурсов из эфира для первого перса"

    jelly()
    morph()
    selected()
    # ferera()
    # ferilla()
    # grifon()
    # anis()
    # sil_stih()
    veton()
    # paporotnik()
    # diamond()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def osn():
    # pers1()
    # craft_pers1()
    # pers2()
    # craft()
    pers3()
    craft()
    pers4()
    craft()
    pers5()
    craft()
    pers6()
    craft()
    pers7()
    craft()
    pers8()
    craft()
    time.sleep(610)
def osn_sklad():
    "функция сбора ресурсов после крафта"
    pers2()
    sklad()
    pers3()
    sklad()
    pers4()
    sklad()
    pers5()
    sklad()
    pers6()
    sklad()
    pers7()
    sklad()
    pers8()
    sklad()
def osn_sklad_take_vortex():
    pers2()
    sklad_take_res()
    pers3()
    sklad_take_res()
    pers4()
    sklad_take_res()
    pers5()
    sklad_take_res()
    pers6()
    sklad_take_res()
    pers7()
    sklad_take_res()
    pers8()
    sklad_take_res()

def craft_sil_sth():
    "функция крафта ресурсов из эфира"
    jelly()
    morph()
    selected()
    sil_stih()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_firilla():
    "функция крафта ресурсов из эфира"
    jelly()
    morph()
    selected()
    ferilla()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_grifon():
    "функция крафта ресурсов из эфира"
    jelly()
    morph()
    selected()
    grifon()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_ferera():
    "функция крафта фереры из эфира"
    jelly()
    morph()
    selected()
    ferera()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_okka():
    "функция крафта окки из эфира"
    jelly()
    morph()
    selected()
    okka()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def craft_runime():
    "функция крафта рунимэ из эфира"
    jelly()
    morph()
    selected()
    runime()
    create_all()
    print('крафчу')
    time.sleep(85)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 1)
    print('нажал esc')
    cross()
    print('нажал крестик')
    exit()

def all_craft_sil_stih():
    "функция крафта всеми персами сильного стихийного камня"
    pers1()
    craft_sil_sth()
    pers2()
    craft_sil_sth()
    pers3()
    craft_sil_sth()
    pers4()
    craft_sil_sth()
    pers5()
    craft_sil_sth()
    pers6()
    craft_sil_sth()
    pers7()
    craft_sil_sth()
    pers8()
    craft_sil_sth()
    time.sleep(610)

def all_cratf_ferilla():
    "функция крафта всеми персами фериллы"
    pers1()
    craft_firilla()
    pers2()
    craft_firilla()
    pers3()
    craft_firilla()
    pers4()
    craft_firilla()
    pers5()
    craft_firilla()
    pers6()
    craft_firilla()
    pers7()
    craft_firilla()
    pers8()
    craft_firilla()
    time.sleep(610)

def all_craft_grifon():
    "функция крафта всеми персами грифонии"
    pers1()
    craft_grifon()
    pers2()
    craft_grifon()
    pers3()
    craft_grifon()
    pers4()
    craft_grifon()
    pers5()
    craft_grifon()
    pers6()
    craft_grifon()
    pers7()
    craft_grifon()
    pers8()
    craft_grifon()
    time.sleep(610)

def all_craft_ferera():
    "функция крафта всеми персами фереры"
    pers1()
    craft_ferera()
    pers2()
    craft_ferera()
    pers3()
    craft_ferera()
    pers4()
    craft_ferera()
    pers5()
    craft_ferera()
    pers6()
    craft_ferera()
    pers7()
    craft_ferera()
    pers8()
    craft_ferera()
    time.sleep(610)

def all_craft_cocktail():
    "функция крафта всеми персами окки и рунимэ"
    pers1()
    craft_okka()
    pers2()
    craft_okka()
    pers3()
    craft_okka()
    pers4()
    craft_okka()
    pers5()
    craft_runime()
    pers6()
    craft_runime()
    pers7()
    craft_runime()
    pers8()
    craft_runime()
    time.sleep(610)

# time.sleep(2)

# osn()
# all_craft_cocktail()
# all_craft_cocktail()
# all_craft_cocktail()
# all_craft_sil_stih()
# all_craft_sil_stih()
# get_position()


# osn()
# osn()

# osn_sklad()
# osn_sklad_take_vortex()

# craft()
# pers2()
# jelly()
# morph()
# selected()
# ferera()
# create_all()

# change_pers()
# get_position()
# exit()
# time.sleep(10)
