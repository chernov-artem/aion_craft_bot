import numpy as np
import cv2

# Загрузка изображений
template = cv2.imread("51.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("calc.jpg")

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск совпадения
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
    cv2.circle(image, pt, 7, (0,0,255), -1)
    cv2.circle(image, pt, 7, (0,0,255), -1)
cv2.rectangle(image, (pt[0] - 2, pt[1] - 2), (pt[0] + 20, pt[1] + 20), (0, 255, 0), 2)

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()