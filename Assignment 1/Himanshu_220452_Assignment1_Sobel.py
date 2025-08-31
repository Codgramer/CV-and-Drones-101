import cv2
import numpy as np

def Sobel(s):
    sobelx = cv2.Sobel(s , cv2.CV_64F , 1 , 0 , ksize = 3)
 
    sobely = cv2.Sobel(s , cv2.CV_64F , 0 , 1 , ksize = 3)

    magnitude = np.sqrt(sobelx**2 + sobely**2)

    cv2.normalize(magnitude , magnitude , 0 , 255 , cv2.NORM_MINMAX)

    magnitude = np.uint8(magnitude)

    cv2.imshow("Edge detected image" , magnitude)
    cv2.waitKey(0)

img = cv2.imread(r"C:\Users\Himanshu\Downloads\put-together-a-perfect-guest-room-1976987-hero-223e3e8f697e4b13b62ad4fe898d492d.jpg")
cv2.imshow("Original image",img)
img = cv2.imread(r"C:\Users\Himanshu\Downloads\put-together-a-perfect-guest-room-1976987-hero-223e3e8f697e4b13b62ad4fe898d492d.jpg", cv2.IMREAD_GRAYSCALE)
Sobel(img)