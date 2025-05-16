import cv2

img = cv2.imread('kiww.jpg')

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Asli", img)
cv2.imshow("Grayscale", gray)
cv2.imwrite("grayscale.jpg", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()