import cv2
import numpy as np
import dlib


cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    _,frame = cap.read()
    
    faces = detector(frame)
    
    cv2.imshow("Frame",frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    