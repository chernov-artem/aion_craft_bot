import pyautogui as pag
import time
import cv2
import numpy as np

def find_coordinates(tmp: bin, screen: bin) -> tuple:
    'функция поиска шаблона на изображении. Возвращает координаты'
    # Преобразование изображения в оттенки серого
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(screen)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        print(pt)
        return pt

time.sleep(2)
# image_location = pag.locateOnScreen('np.png')
# if image_location is not None:
#     print("Image found at ({}, {})".format(image_location.left, image_location.top))
# else:
#     print("Image not found")
# tmp = pag.size()
# print(tmp)
pag.typewrite('o', 0)
time.sleep(1)
sshot = pag.screenshot()
time.sleep(0.2)
image_location = pag.locateOnScreen('change_pers_button.jpg', grayscale=True)
print(image_location)
# if image_location is not None:
#     print("Image found at ({}, {})".format(image_location.left, image_location.top))
# else:
#     print("Image not found")