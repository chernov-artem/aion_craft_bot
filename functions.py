import keyboard
import mouse
import time

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

def exit():
    aion_screen()
    move_and_clic(1317, 992)
    move_and_clic(1305, 937)
    time.sleep(0.7)
    mouse.move(973, 530, 0.2)
    mouse.click('left')

# get_position()
# choise_last()
# time.sleep(10)
exit()