import keyboard
import mouse
import time
import images
import pyautogui as pag
# keyboard.write('Hello!', 0.1)



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

def pers1():
    "функция выбора перса"
    xy_tmp = images.pers1()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers2():
    "функция выбора перса"
    xy_tmp = images.pers2()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers3():
    "функция выбора перса"
    xy_tmp = images.pers3()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers4():
    "функция выбора перса"
    xy_tmp = images.pers4()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers5():
    "функция выбора перса"
    xy_tmp = images.pers5()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers6():
    "функция выбора перса"
    xy_tmp = images.pers6()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers7():
    "функция выбора перса"
    xy_tmp = images.pers7()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(11)

def pers8():
    "функция выбора перса"
    xy_tmp = images.pers8()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
        mouse.click('left')
        mouse.click('left')
    else:
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

def ferera_icon():
    "функция нажатия на фереру"
    xy_tmp = images.ferera_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_right_clic(x + 34, y + 11)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.43)
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
        mouse.click('left')
        # mouse.click('left')
    else:
        move_and_clic(1200, 500)
    time.sleep(0.9)


def exit():
    print('выход запущен')
    pag.typewrite('o', 0)
    print('нажал o')
    time.sleep(0.6)
    if images.change_pers() == None:
        pag.typewrite('o', 0)
        print('нажал o ещё раз')
        time.sleep(0.55)
        change_pers()
    else:
        change_pers()
    time.sleep(15)

def sklad():
    pag.typewrite('9', 1)
    pag.typewrite('c', 1)
    sklad_leg_btn()
    ferera_icon()
    time.sleep(0.3)
    ferera_icon()


def craft():
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

def osn():
    # pers1()
    # craft()
    # pers2()
    # craft()
    # pers3()
    # craft()
    # pers4()
    # craft()
    pers5()
    craft()
    pers6()
    craft()
    pers7()
    craft()
    pers8()
    craft()



time.sleep(2)

osn()

# craft()
# sklad()
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
