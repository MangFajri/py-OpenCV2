import cv2
import os

# Baca gambar
img1 = cv2.imread('background.jpg')
img2 = cv2.imread('logo.jpg')

# Cek apakah gambar berhasil dibaca
if img1 is None:
    print("❌ Gagal membaca 'background.jpg'. Pastikan file ada dan path benar.")
    exit()

if img2 is None:
    print("❌ Gagal membaca 'logo.png'. Pastikan file ada dan path benar.")
    exit()

# Resize logo agar sama ukuran dengan background
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Blending dengan rasio 60% (img1) dan 40% (img2)
blended = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# Tampilkan hasil
cv2.imshow("Gambar 1", img1)
cv2.imshow("Gambar 2", img2)
cv2.imshow("Blended", blended)

# Simpan hasil
cv2.imwrite("blended_result.jpg", blended)

cv2.waitKey(0)
cv2.destroyAllWindows()
