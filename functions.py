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

def aion_screen():
    mouse.move(419, 1052, 0.2)
    mouse.click('left')

def choise_last():
    aion_screen()
    mouse.move(1532, 850, 0.2)
    time.sleep(0.7)
    mouse.click('left')
    time.sleep(0.4)
    mouse.click('left')

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
    xy_tmp = images.ferera()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.4)

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

def exit():
    print('выход запущен')
    pag.typewrite('o', 0)
    print('нажал o')
    time.sleep(0.6)
    change_pers()
    time.sleep(15)

def sklad():
    pag.typewrite('9', 1)
    pag.typewrite('c', 1)


def craft():
    jelly()
    morph()
    selected()
    ferera()
    create_all()
    print('крафчу')
    time.sleep(90)
    print('закончилась пауза, запускаю выход')
    pag.typewrite('esc', 0)
    print('нажал esc')
    exit()




time.sleep(2)

# craft()
sklad()

# jelly()
# morph()
# selected()
# ferera()
# create_all()

# change_pers()
# get_position()
# exit()
# time.sleep(10)
