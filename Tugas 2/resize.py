import cv2

img = cv2.imread('kiww.jpg')

# Resize ke 100x100 px
resized = cv2.resize(img, (100, 100))
resized = cv2.resize(img, (300, 300))
resized = cv2.resize(img, (500, 500))

cv2.imshow("Original", img)
cv2.imshow("Resized 100x100", resized)
cv2.imshow("Resized 300x300", resized)
cv2.imshow("Resized 500x500", resized)
cv2.imwrite("resized_100x100.jpg", resized)
cv2.imwrite("resized_300x300.jpg", resized)
cv2.imwrite("resized_500x500.jpg", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()