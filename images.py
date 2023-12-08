import pyautogui as pag
import time

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