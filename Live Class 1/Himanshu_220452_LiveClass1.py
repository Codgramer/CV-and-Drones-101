import cv2
import numpy as np

def solve(s):
    img = cv2.imread(s)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    f = np.fft.fft2(img1)
    fshift = np.fft.fftshift(f)
    mag = 20 * np.log(np.abs(fshift))

    magnitude_spectrum = np.uint8(mag)
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum)
    cv2.waitKey(0)

# Example usage
path = "C:/Users/Himanshu/Downloads/Arrow.jpg"
solve(path)
