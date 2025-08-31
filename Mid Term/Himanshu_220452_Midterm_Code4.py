import cv2
import numpy as np

def shape(s):
    original_image = cv2.imread(s)

    scale_factor = 2

    resized_image = cv2.resize(original_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    edges = cv2.Canny(blurred_image, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shape_names = {3: "Triangle", 4: "Quadrilateral", 5: "Pentagon", 6: "Hexagon", 7: "Heptagon", 8: "Octagon", 9: "Nonagon"}

    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

    all_shapes_info = []

    for i, contour in enumerate(sorted_contours):
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        num_sides = len(approx)

        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        shape_name = shape_names.get(num_sides, "Unknown")
        all_shapes_info.append({"Shape": shape_name, "Center": (cX, cY)})

        cv2.putText(resized_image, f"{shape_name}", (cX - 30, cY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    for i, contour in enumerate(sorted_contours[:2]):
        # Get the center of the shape
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.putText(resized_image, f"Largest-{i+1} - Center: ({cX}, {cY})", (cX - 60, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(resized_image, (cX, cY), 5, (0, 255, 0), -1)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Shapes and Centers', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return all_shapes_info

image_path = r"C:\Users\Himanshu\Downloads\images.png"
all_shapes_info = shape(image_path)

