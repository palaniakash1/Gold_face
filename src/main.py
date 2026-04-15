import cv2
import numpy as np
import dlib
from math import hypot
import os
from glob import glob

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

necklace_paths = sorted(glob(os.path.join(project_root, "assets/necklace/*.png")))
earing_paths = sorted(glob(os.path.join(project_root, "assets/earing/*.jpg")))

necklace_images = [cv2.imread(path) for path in necklace_paths]
earing_images = [cv2.imread(path) for path in earing_paths]

necklace_images = [img for img in necklace_images if img is not None]
earing_images = [img for img in earing_images if img is not None]

if not necklace_images or not earing_images:
    print("Error: No images loaded from 'necklace/' or 'earing/' folders.")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam. Please check if a webcam is connected.")
    exit()

ret, frame = cap.read()
if not ret or frame is None:
    print(
        "Error: Cannot read from webcam. Please check if a webcam is connected and working."
    )
    cap.release()
    exit()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    os.path.join(project_root, "shape_predictor_68_face_landmarks.dat")
)

jewelry_index = 0

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_frame)
    frame_h, frame_w = frame.shape[:2]

    jewel_img = necklace_images[jewelry_index % len(necklace_images)]
    earring_img = earing_images[jewelry_index % len(earing_images)]

    h, w, _ = earring_img.shape
    left_earing_img = earring_img[:, : w // 2]
    right_earing_img = earring_img[:, w // 2 :]

    for face in faces:
        landmarks = predictor(gray_frame, face)

        left_chin = (landmarks.part(4).x, landmarks.part(4).y)
        right_chin = (landmarks.part(12).x, landmarks.part(12).y)
        center_chin = (landmarks.part(8).x, landmarks.part(8).y)

        left_ear = (landmarks.part(1).x, landmarks.part(1).y)
        right_ear = (landmarks.part(15).x, landmarks.part(15).y)
        center_left_ear = (landmarks.part(2).x, landmarks.part(2).y)
        center_right_ear = (landmarks.part(14).x, landmarks.part(14).y)

        chin_width = int(
            hypot(left_chin[0] - right_chin[0], left_chin[1] - right_chin[1])
        )
        chin_height = int(chin_width * 0.96)
        distance = 80

        chin_top_left = (
            int(center_chin[0] - chin_width / 2),
            int(center_chin[1] - chin_height / 2) + distance,
        )

        x1, y1 = max(0, chin_top_left[0]), max(0, chin_top_left[1])
        x2 = min(x1 + chin_width, frame_w)
        y2 = min(y1 + chin_height, frame_h)

        resized_jewel = cv2.resize(jewel_img, (x2 - x1, y2 - y1))
        mask_jewel = cv2.cvtColor(resized_jewel, cv2.COLOR_BGR2GRAY)
        _, mask_jewel = cv2.threshold(mask_jewel, 25, 255, cv2.THRESH_BINARY_INV)

        roi_chin = frame[y1:y2, x1:x2]
        roi_bg = cv2.bitwise_and(roi_chin, roi_chin, mask=mask_jewel)
        dst = cv2.add(roi_bg, resized_jewel)
        frame[y1:y2, x1:x2] = dst

        full_ear_width = int(
            hypot(left_ear[0] - right_ear[0], left_ear[1] - right_ear[1])
        )
        ear_width = int(full_ear_width * 0.25)
        ear_height = int(ear_width * 1.5)

        ear_offset_x = 10
        ear_offset_y = 5
        distance_1 = 30

        def place_earring(center_ear, earring_img, offset_x):
            top_left = (
                int(center_ear[0] - ear_width / 2) - offset_x,
                int(center_ear[1] - ear_height / 2) + ear_offset_y + distance_1,
            )
            x1 = max(0, top_left[0])
            y1 = max(0, top_left[1])
            x2 = min(x1 + ear_width, frame_w)
            y2 = min(y1 + ear_height, frame_h)

            resized_earring = cv2.resize(earring_img, (x2 - x1, y2 - y1))
            mask = cv2.cvtColor(resized_earring, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY_INV)

            roi = frame[y1:y2, x1:x2]
            if roi.shape[:2] == mask.shape:
                roi_bg = cv2.bitwise_and(roi, roi, mask=mask)
                dst = cv2.add(roi_bg, resized_earring)
                frame[y1:y2, x1:x2] = dst

        place_earring(center_left_ear, left_earing_img, ear_offset_x)
        place_earring(center_right_ear, right_earing_img, -10)

    cv2.imshow("Jewelley", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("n"):
        jewelry_index += 1

cap.release()
cv2.destroyAllWindows()
