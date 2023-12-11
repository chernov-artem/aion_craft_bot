import pyautogui as pag
import time
import cv2
import numpy as np

def find_coordinates(tmp: str) -> tuple:
    'функция поиска шаблона на изображении. Возвращает координаты'
    # Преобразование изображения в оттенки серого
    time.sleep(0.3)
    pag.screenshot('screenshot.png')
    time.sleep(0.3)
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        return pt

def pers1():
    return find_coordinates('images/SpielSucht.png')

def pers2():
    return find_coordinates('images/DeadPonyClub.png')

def pers3():
    return find_coordinates('images/HungaMunga.png')

def pers4():
    return find_coordinates('images/Rebyata.png')

def pers5():
    return find_coordinates('images/KillClericFirst.png')

def pers6():
    return find_coordinates('images/Huanito.png')

def pers7():
    return find_coordinates('images/Huanita.png')

def pers8():
    return find_coordinates('images/spbscale.png')

def cross():
    return find_coordinates('images/cross.png')

def change_pers():
    return find_coordinates('images/change_pers_button.png')

def morph():
    return find_coordinates('images/morph.png')

def selected():
    return find_coordinates('images/selected.png')

def jelly():
    return find_coordinates('images/jelly.png')

def ferera():
    return find_coordinates('images/ferera.png')

def create_all():
    return find_coordinates('images/create_all.png')

def sklad_leg_btn():
    return find_coordinates('images/sklad_leg_btn.png')

def ferera_icon():
    return find_coordinates('images/ferera_icon.png')



# time.sleep(2)
# image_location = pag.locateOnScreen('np.png')
# if image_location is not None:
#     print("Image found at ({}, {})".format(image_location.left, image_location.top))
# else:
#     print("Image not found")
# tmp = pag.size()
# print(tmp)

# pag.typewrite('o', 0)

# change_pers()


# if image_location is not None:
#     print("Image found at ({}, {})".format(image_location.left, image_location.top))
# else:
#     print("Image not found")