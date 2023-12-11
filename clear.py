import numpy as np
import cv2

# Загрузка изображений
template = cv2.imread("51.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("calc.jpg")
print(type(template))

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск совпадения
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    # print(pt)
    cv2.circle(image, pt, 7, (0,0,255), -1)
    # cv2.circle(image, (0, 0), 7, (255,0,0), -1)
    cv2.rectangle(image, (pt[0] - 2, pt[1] - 2), (pt[0] + 20, pt[1] + 20), (0, 255, 0), 2)

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

coord = find_coordinates('51.jpg', 'calc.jpg')
print(coord[0], coord[1])
# cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()