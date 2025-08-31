import cv2

def solve(s):
    edges = cv2.Canny(s,50,150)

    cv2.imshow('Original Image', s)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)



img = cv2.imread(r"C:\Users\Himanshu\Downloads\6641728-beautiful-park.jpg")
solve(img)