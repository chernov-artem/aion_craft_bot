import time
import mouse

import images

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

def ferera_icon():
    "функция нажатия на фереру"
    xy_tmp = images.ferera_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_right_clic(x + 34, y + 11)
        mouse.move(44, 44)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.43)

def blue_grass_icon():
    "функция нажатия на синюю траву(манна)"
    xy_tmp = images.blue_grass_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_right_clic(x + 34, y + 11)
        mouse.move(44, 44)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.46)

def red_grass_icon():
    "функция нажатия на красную траву(hp)"
    xy_tmp = images.red_grass_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_right_clic(x + 34, y + 11)
        mouse.move(44, 44)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.47)

def sil_stih_icon():
    "функция нажатия на сильный стихийный камень"
    xy_tmp = images.sil_stih_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_right_clic(x + 34, y + 11)
        mouse.move(44, 44)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.47)

def vortex40_icon():
    "функция нажатия на белый эфир 40"
    xy_tmp = images.vortex40_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        razbib(x + 34, y + 11)
        mouse.move(44, 44)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.47)

