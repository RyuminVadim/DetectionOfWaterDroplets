import cv2
import matplotlib.pyplot as plt

image = cv2.imread("ex_1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
plt.imshow(binary, cmap = "gray")
plt.show()

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
plt.imshow(image)
plt.show()
cv2.imwrite("result.jpg", image)
