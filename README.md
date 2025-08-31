EEA Winter Project

This project explores the intersection of Computer Vision (CV) and Drone Technology, focusing on real-time image processing and autonomous drone navigation. The pipeline includes:

Image filtering, Fourier Transform, hybrid imaging, and edge detection (Sobel & Canny)

Color segmentation, Hough Transforms, and contour analysis for shape and line detection

Camera calibration using intrinsic matrix & distortion coefficients with chessboard patterns

ArUco marker detection for precise localization and navigation

Autonomous control of Tello Drone via the djitellopy library


Features

🖼️ Image enhancement & filtering

📐 Line, shape & color recognition

🎯 Camera calibration & distortion correction

🛰️ Real-time ArUco marker-based drone navigation

🕹️ PID-based stable flight control


Results

Accurate detection of geometric shapes and contours

Corrected lens distortions and skew in captured frames

Achieved real-time marker tracking for stable navigation

Successfully demonstrated autonomous flight commands on Tello Drone


Tech Stack

Languages: Python

Libraries: OpenCV, PIL, NumPy, djitellopy, matplotlib

Hardware: Tello Drone, Webcam
