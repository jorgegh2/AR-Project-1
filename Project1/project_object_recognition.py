import cv2
import numpy as np

def ProjectObjectRecognition(image_path, target_path, threshold):


    image = cv2.imread(image_path)
    target = cv2.imread(target_path)

    image = image / 255 #no se si es necesario ^^
    
    cv2.imshow('Image', image)
    cv2.imshow('Target', target)


    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
            
ProjectObjectRecognition("img1.png", "t1-img1.png", 0.1)

