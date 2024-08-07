import pyautogui as pag
import time
import cv2
import numpy as np

def find_coordinates(tmp: str, y : int = 0) -> tuple:
    'функция поиска шаблона на изображении. Возвращает координаты'
    # Преобразование изображения в оттенки серого
    time.sleep(0.3)
    print('делаю скрин')
    sc = pag.screenshot(region=(0, int(y), 1650, int(1050 - y)))
    sc.save('screenshot.png')
    time.sleep(0.3)
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)
    print(loc)

    for pt in zip(*loc[::-1]):
        return pt

def find_second_coordinates(tmp: str) -> tuple:
    """функция поиска на изображении координат второго объекта
    сначала ищет координаты первого объекта, потом делает скриншот на 30 пикселей ниже найденых координат
    и снова ищет координаты шаблона"""
    x,y = find_coordinates(tmp)
    sc = pag.screenshot(region=(0, int(y + 30), int(1650 - x), int(1050 - y)))
    sc.save('screenshot2.png')
    # дальше идет код из find_coordinates
    time.sleep(0.3)
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread('screenshot2.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)
    print(loc)
    # добавляем координаты старые координаты y к новым координатам y
    for pt0 in zip(*loc[::-1]):
        pass

    pt = (pt0[0] + 2, pt0[1] + y + 30)

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

def menu_btn():
    return find_coordinates('images/menu_btn.png')
def sist_menu():
    return find_coordinates('images/sist_menu.png')
def prinat_btn():
    return find_coordinates('images/prinat_btn.png')

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

def ferilla():
    return find_coordinates('images/ferilla.png')

def grifon():
    return find_coordinates('images/grifonia.png')

def anis():
    return find_coordinates('images/anis.png')

def sil_stih():
    return find_coordinates('images/silstih.png')

def veton():
    return find_coordinates('images/veton.png')

def paporotnik():
    return find_coordinates('images/paporotnik.png')

def okka():
    return find_coordinates('images/okka.png')

def runime():
    return find_coordinates('images/runime.png')
def diamond():
    return find_coordinates('images/diamond.png')

def silver():
    return find_coordinates('images/silver.png')
def iron_ore():
    return find_coordinates('images/iron_ore.png')

def rukon():
    return find_coordinates('images/rukon.png')
def create_all():
    return find_coordinates('images/create_all.png')

def sklad_leg_btn():
    return find_coordinates('images/sklad_leg_btn.png')

def ferera_icon():
    return find_coordinates('images/ferera_icon.png')

def blue_grass_icon():
    return find_coordinates('images/blue_grass_icon.png')
def red_grass_icon():
    return find_coordinates('images/red_grass_icon.png')
def sil_stih_icon():
    return find_coordinates('images/sil_stih_icon.png')
def vortex40_icon():
    return find_coordinates('images/vortex40g.png')



