import cv2
import numpy as np
import matplotlib.pyplot as plt

rotated_0_deg = None
rotated_90_deg = None
rotated_180_deg = None
rotated_270_deg = None

def rotate(img, y):
    rows, cols, _ = img.shape
    center = (cols // 2, rows // 2)
    matrix = cv2.getRotationMatrix2D(center, y, 1.0)
    rotated_img = cv2.warpAffine(img, matrix, (cols, rows))
    return rotated_img

def rotatedFlags():
    global rotated_0_deg, rotated_90_deg, rotated_180_deg, rotated_270_deg
    original_image = cv2.imread(r"C:\Users\Himanshu\Downloads\Figure_1.png")
    rotated_0_deg = rotate(original_image, 0)
    rotated_90_deg = rotate(original_image, 90)
    rotated_180_deg = rotate(original_image, 180)
    rotated_270_deg = rotate(original_image, 270)

def horizontal_traversal(image):

    midline_index = image.shape[0] // 2

    for i in range(image.shape[1]):
        pixel_color = image[midline_index,i]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue
        else:
            if np.array_equal(pixel_color, [52, 153, 255]):
                hor_orientation = "90deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                hor_orientation = "270deg"
                break    
    return hor_orientation

def vertical_traversal(image):

    midline_index = image.shape[1] // 2

    for i in range(image.shape[0]):
        pixel_color = image[i, midline_index]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue

        else:
            if np.array_equal(pixel_color,[52, 153, 255]):
                ver_orientation = "0deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                ver_orientation = "180deg"
                break
            elif np.array_equal(pixel_color, [255,255,255]):
                ver_orientation = horizontal_traversal(image)
                break
    
    return ver_orientation

def unskew(s):
    
    img = cv2.imread(s)
    img = cv2.resize(img,(150,150))
    rotatedFlags()
    
    orientation = vertical_traversal(img)
    print("skewed image orietation resembles " + orientation + " of the reference image")
    if orientation == "0deg":
        cv2.imshow("Unskewed",rotated_0_deg)
    elif orientation == "90deg":
        cv2.imshow("Unskewed",rotated_90_deg)
    elif orientation == "180deg":
        cv2.imshow("Unskewed",rotated_180_deg)
    elif orientation == "270deg":
        cv2.imshow("Unskewed",rotated_270_deg)
    cv2.imshow("Skewed",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

s = r"C:\Users\Himanshu\Downloads\Test Case 5.jpg"
unskew(s)
