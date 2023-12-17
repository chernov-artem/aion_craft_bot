import keyboard
import mouse
import time
import images
import pyautogui as pag

import icons

# mouse.move(419, 1052, 0.2)
# mouse.click('left')
# time.sleep(2)
# mouse.move(877, 976, 0.2)
# time.sleep(2)
# mouse.click('left')

def get_position():
    time.sleep(2)
    current_cursor = mouse.get_position()
    print(current_cursor)

def move_and_clic(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('left')
    time.sleep(0.7)

def move_and_right_clic(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('right')
    time.sleep(0.7)

def razbib(x: int, y: int):
    mouse.move(x, y, 0.2)
    time.sleep(0.3)
    pag.keyDown('Shift')
    mouse.click('right')
    time.sleep(0.15)
    pag.keyUp('Shift')
    time.sleep(0.3)

def pers1():
    "функция выбора 1 перса"
    xy_tmp = images.pers1()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers1()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers1()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers2():
    "функция выбора 2 перса"
    xy_tmp = images.pers2()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers2()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers2()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers3():
    "функция выбора 3 перса"
    xy_tmp = images.pers3()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers3()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers3()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers4():
    "функция выбора 4 перса"
    xy_tmp = images.pers4()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers4()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers4()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers5():
    "функция выбора 5 перса"
    xy_tmp = images.pers5()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers5()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers5()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers6():
    "функция выбора 6 перса"
    xy_tmp = images.pers6()
    if xy_tmp != None:
        print('хуанито 1 попытка')
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        print('хуанито 2 попытка')
        time.sleep(3)
        xy_tmp = images.pers6()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        print('хуанито 3 попытка')
        time.sleep(3)
        xy_tmp = images.pers6()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers7():
    "функция выбора 7 перса"
    xy_tmp = images.pers7()
    if xy_tmp != None:
        print('хуанита 1 попытка')
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        print('хуанита 2 попытка')
        time.sleep(3)
        xy_tmp = images.pers7()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        print('хуанита 3 попытка')
        time.sleep(3)
        xy_tmp = images.pers7()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)

def pers8():
    "функция выбора 8 перса"
    xy_tmp = images.pers8()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    elif xy_tmp == None:
        time.sleep(3)
        xy_tmp = images.pers8()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        time.sleep(3)
        xy_tmp = images.pers8()
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
        move_and_clic(1200, 500)
    time.sleep(11)
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
    "функция нажатия на кнопку изготовить всё"
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
    pag.typewrite('9', 1)
    time.sleep(0.44)
    pag.typewrite('c', 1)
    sklad_leg_btn()
    icons.vortex40_icon()
    take20()
    cross()
    jelly()
    morph()
    selected()
    # ferera()
    # ferilla()
    # grifon()
    # anis()
    # sil_stih()
    # veton()
    # paporotnik()
    diamond()
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
    # veton()
    # paporotnik()
    diamond()
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
    pers1()
    craft_pers1()
    pers2()
    craft()
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
    time.sleep(800)
def osn_sklad():
    "функция сбора ресурсов после крафта"
    # pers2()
    # sklad()
    # pers3()
    # sklad()
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
    "функция крафта ресурсов из эфира"
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

def all_sil_stih():
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
    time.sleep(800)

def all_sil_ferilla():
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
    time.sleep(800)

def all_sil_grifon():
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
    time.sleep(800)

def all_sil_ferera():
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
    time.sleep(800)

time.sleep(2)

# icons.blue_grass_icon()

all_sil_stih()
all_sil_stih()
all_sil_stih()
all_sil_ferilla()
all_sil_ferilla()
all_sil_grifon()
all_sil_grifon()
all_sil_ferera()
all_sil_ferera()
all_sil_ferera()
all_sil_ferera()

# osn()
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
