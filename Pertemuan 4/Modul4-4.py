import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
image = cv2.imread('Dadu_fireblue.jpeg', 0)

# Melakukan FFT
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Menghitung magnitude spectrum
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Menampilkan gambar asli dan magnitude spectrum
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum')
plt.show

# Menampilkan hasil
cv2.imshow('Original Image', image)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()