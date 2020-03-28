import cv2
import numpy as np

def ObjectRecognition():

    image, target, threshold = GetInput()

    image_color = cv2.imread(image)
    target_color = cv2.imread(target)
    image_gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    target_gray = cv2.imread(target, cv2.IMREAD_GRAYSCALE)


    matching_map = ComputeMatchingMap(image_gray, target_gray)
    CheckResult(matching_map, threshold, image_color, target_gray)

    cv2.imshow('Image', image_color)
    cv2.imshow('Target', target_color)
    cv2.imshow("Matching Map", matching_map)
    
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()


def GetInput():
    image = input("Input image: ")
    target = input("Target image: ")
    threshold = input("Detection threshold: ")

    return image, target, threshold


def ComputeMatchingMap(image_gray, target_gray):
    image_rows, image_cols = image_gray.shape
    target_rows, target_cols = target_gray.shape

    matching_map = np.zeros((image_rows - target_rows + 1, image_cols - target_cols + 1))
    matching_map_rows, matching_map_cols = matching_map.shape

    for i in range(matching_map_rows):
        for j in range(matching_map_cols):
            for x in range(target_rows):
                for y in range(target_cols):
                    matching_map[i, j] += np.square(int(target_gray[y,x]) - int(image_gray[i + y, j + x]))


    matching_map /= matching_map.max()

    return matching_map


def CheckResult(matching_map, threshold, image_color, target_color):
    counter = 0

    matching_map_rows, matching_map_cols = matching_map.shape
    target_rows, target_cols = target_color.shape

    for i in range(0,matching_map_rows):
        for j in range(0,matching_map_cols):
            if matching_map[i, j] / matching_map.max() <= float(threshold):
                cv2.rectangle(image_color, (j, i), (j + target_cols, i + target_rows), (0, 255, 0), 2)
                counter += 1

    is_target_found = np.zeros((40, 325, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if counter > 0: 
        cv2.putText(is_target_found, "TARGETS FOUND: " + str(counter), (5, 30), font, 1, (0, 255, 0), 2)

    else:
        cv2.putText(is_target_found, "TARGET NOT FOUND", (5, 30), font, 1, (0, 0, 255), 2)

    cv2.imshow("Result", is_target_found)


ObjectRecognition()

