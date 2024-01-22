import mouse
import time
import pyautogui as pag
def move_and_clic(x: int, y: int):
    "кликает по заданным координатам"
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('left')
    time.sleep(0.7)

def move_and_right_clic(x: int, y: int):
    "делает клик ПКМ по заданным координатам"
    mouse.move(x, y, 0.2)
    time.sleep(0.7)
    mouse.click('right')
    time.sleep(0.7)

def razbib(x: int, y: int):
    "функция позволяет разбить ресурс на 2 ячейки"
    mouse.move(x, y, 0.2)
    time.sleep(0.3)
    pag.keyDown('Shift')
    mouse.click('right')
    time.sleep(0.15)
    pag.keyUp('Shift')
    time.sleep(0.3)