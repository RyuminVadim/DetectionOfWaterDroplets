import cv2
from sympy import Point, Ellipse
import numpy as np

image = cv2.imread('ex_1.jpg', 0)
image1 = cv2.imread('ex_1.jpg', 1)

x, y = image.shape

median = cv2.GaussianBlur(image, (9, 9), 0)
median1 = cv2.GaussianBlur(image, (21, 21), 0)

a = median1 - median
c = 255 - a

ret, thresh1 = cv2.threshold(c, 12, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(thresh1, kernel, iterations=1)
kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
cv2.imwrite('ex_1_changed.jpg', opening)

contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

c = np.size(contours[:])

Blank_window = np.zeros([x, y, 3])
Blank_window = np.uint8(Blank_window)

contours = contours[0]
for contour in contours:
    if np.size(contour[0][0]) > 200:
        ellipse = cv2.fitEllipse(contour)
        (center, axes, orientation) = ellipse
        majoraxis_length = max(axes)
        minoraxis_length = min(axes)

        eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
        if (eccentricity < 0.8):
            cv2.drawContours(image1, contours, contour[0][0], (255, 1, 255), 3)

    elif np.size(contour[0][1]) > 200:
        ellipse = cv2.fitEllipse(contour)
        (center, axes, orientation) = ellipse
        majoraxis_length = max(axes)
        minoraxis_length = min(axes)

        eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
        if (eccentricity < 0.8):
            cv2.drawContours(image1, contours, contour[0][1], (255, 1, 255), 3)
cv2.imwrite('res.jpg', image1)
