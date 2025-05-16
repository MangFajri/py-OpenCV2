import cv2

# baca gambar
img = cv2.imread('kiww.jpg')
# tampilkan gambar asli
print("gambar asli:", img.shape) # (tinggi, lebar, channel)
# crop gambar
crop = img[100:700, 200:700] 

# tampilkan gambar hasil
cv2.imshow("Asli", img)
cv2.imshow("Crop", crop)
cv2.imwrite("wajah_crop.jpg", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()