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

def change_pers():
    return find_coordinates('images/change_pers_button.png')

def morph():
    return find_coordinates('images/morph.png')

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