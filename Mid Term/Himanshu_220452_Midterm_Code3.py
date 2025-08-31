import cv2
import numpy as np

def color(s):
    target_color='blue'
    original_image = cv2.imread(s)
    original_image = cv2.resize(original_image,(500,500))


    img_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    if target_color == 'red':
        lower_bound = np.array([100, 0, 0], dtype=np.uint8)
        upper_bound = np.array([255, 100, 100], dtype=np.uint8)
    elif target_color == 'green':
        lower_bound = np.array([0, 100, 0], dtype=np.uint8)
        upper_bound = np.array([100, 255, 100], dtype=np.uint8)
    elif target_color == 'blue':
        lower_bound = np.array([0, 0, 100], dtype=np.uint8)
        upper_bound = np.array([100, 100, 255], dtype=np.uint8)
    else:
        print("Invalid target color.")
        return

    mask = cv2.inRange(img_rgb, lower_bound , upper_bound)

    contours, hierarchy = cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
 
    img_contour = original_image.copy()
    cv2.drawContours(img_contour, contours, -1, (255, 0, 0), 2)
    
    
    shade = cv2.imread(r"C:\Users\Himanshu\OneDrive - IIT Kanpur\Pictures\Screenshots\Screenshot 2024-02-07 020214.png")
    shade = cv2.resize(shade,(500,500))
    cv2.imshow('shade' , shade)
    cv2.imshow('Original image', original_image)
    cv2.imshow('Original Image with Contours', img_contour)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r"C:\Users\Himanshu\Downloads\learning-toys-color-shapes-set-for-kids-education-vector-8492500.jpg"
color(image_path)
