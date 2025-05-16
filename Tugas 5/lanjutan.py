import cv2
import numpy as np

# Fungsi bantu untuk menambahkan teks ke gambar
def tambah_teks(gambar, teks):
    posisi = (20, 40)  # x, y
    font = cv2.FONT_HERSHEY_SIMPLEX
    ukuran = 1.2
    warna = (255, 255, 255)  # putih
    tebal = 2
    cv2.putText(gambar, teks, posisi, font, ukuran, warna, tebal)
    return gambar

# Baca dua gambar
img1 = cv2.imread('logo2.jpg')
img2 = cv2.imread('logo.jpg')

# Cek apakah gambar berhasil dibaca
if img1 is None or img2 is None:
    print("❌ Pastikan file 'background.jpg' dan 'logo.png' tersedia.")
    exit()

# Samakan ukuran
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Gambar asli
original = tambah_teks(img1.copy(), "Asli")

# Crop bagian tengah dari img1
h, w = img1.shape[:2]
crop = img1[h//4:3*h//4, w//4:3*w//4]
crop = cv2.resize(crop, (w, h))
crop = tambah_teks(crop, "Crop")

# Resize img2 ke kecil lalu besar lagi
resized = cv2.resize(img2_resized, (w//2, h//2))
resized = cv2.resize(resized, (w, h))
resized = tambah_teks(resized, "Resize")

# Blending img1 dan img2
blended = cv2.addWeighted(img1, 0.6, img2_resized, 0.4, 0)
blended = tambah_teks(blended, "Blending")

# Gabungkan ke kolase
top = np.hstack((original, crop))
bottom = np.hstack((resized, blended))
kolase = np.vstack((top, bottom))

# Tampilkan dan simpan
cv2.imshow("Kolase", kolase)
cv2.imwrite("kolase_result.jpg", kolase)

cv2.waitKey(0)
cv2.destroyAllWindows()
