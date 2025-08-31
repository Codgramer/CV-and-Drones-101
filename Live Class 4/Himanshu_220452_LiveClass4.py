import cv2
import numpy as np 
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

def aruco_display(corners, ids, rejected, image):
    if len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            topRight = (int(topRight[0]), int(topRight[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
            cX = int((topLeft[0] + bottomRight[0] + topRight[0] + bottomLeft[0]) / 4)
            cY = int((topLeft[1] + bottomLeft[1] + bottomRight[1] + topRight[1]) / 4)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
            print("[Inference] Aruco marker ID: {}".format(markerID))

    return image

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
arucoParams =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, arucoParams)

img=cv2.imread(r"C:\Users\Himanshu\Downloads\xmxTY.png")
h,w,_=img.shape
width=400
height=int(width*(h/w))
img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
print(ids)
detected_markers=aruco_display(corners,ids,rejected,img)
cv2.imshow("Detected_Markers",detected_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()

def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    arucoDict = cv2.aruco.getPredefinedDictionary(aruco_dict_type)
    arucoParams = cv2.aruco.DetectorParameters_create()
    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, arucoDict, parameters=arucoParams)

    if len(corners) > 0:
        for i in range(0, len(ids)):
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 50, matrix_coefficients, distortion_coefficients)
            cv2.aruco.drawDetectedMarkers(frame, corners)
            cv2.aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 5)
            print(tvec)

    return frame


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():
    ret, img = cap.read()
    h, w, _ = img.shape
    width = 1000
    height = int(width * (h / w))
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
    intrinsic_camera = np.array(((207.66132141, 0, 251.41218615), (0, 205.751007, 338.91119239), (0, 0, 1)))
    distortion = np.array((0.07640411, -0.06229856, 0.01462332, 0.0039293, 0.00467759))

    detected_markers = pose_estimation(img, cv2.aruco.DICT_4X4_50, intrinsic_camera, distortion)
    cv2.imshow("Image", detected_markers)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()