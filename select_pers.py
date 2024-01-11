import time
import mouse

import images
from base_functions import move_and_clic
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

time.sleep(2)
pers3()