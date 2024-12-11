import torch
from matplotlib import pyplot as plt
import cv2
import numpy as np
import pytesseract
from test import video 

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load Custom YOLOv5 Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='last.pt', force_reload=True)

video_path='t1.mp4'
# Video capture
cap = cv2.VideoCapture(video_path)  # Change to a video file path if needed

# Labels for detection
labels = ['Helmet', 'Person', 'Motorcycle', 'Vehicle registration plate']

# Tracking variables
detected_plates = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv5 model on the current frame
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()  # Bounding box results

    for detection in detections:
        x1, y1, x2, y2, conf, class_id = detection
        label = labels[int(class_id)]

        if label == 'Motorcycle':
            motorcycle_detected = True  # Detect motorcycle
            helmet_detected = False
            license_plate_text = None

            # Nested check for Helmet
            for detection_h in detections:
                x1_h, y1_h, x2_h, y2_h, conf_h, class_id_h = detection_h
                label_h = labels[int(class_id_h)]

                if label_h == 'Helmet':
                    helmet_detected = True
                    print("Helmet detected")
                    break  # Exit the loop as helmet is detected

            if not helmet_detected:
                # Nested check for Vehicle registration plate
                for detection_p in detections:
                    x1_p, y1_p, x2_p, y2_p, conf_p, class_id_p = detection_p
                    label_p = labels[int(class_id_p)]

                    if label_p == 'Vehicle registration plate':
                        # Extract region of interest (ROI) for the license plate
                        plate_roi = frame[int(y1_p):int(y2_p), int(x1_p):int(x2_p)]

                        # Preprocess the ROI for OCR
                        gray = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
                        resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
                        thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                       cv2.THRESH_BINARY, 11, 2)
                        thresh = cv2.medianBlur(thresh, 3)

                        # Use Tesseract OCR to read the text
                        license_plate_text = pytesseract.image_to_string(
                            thresh, config='--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                        )
                        print("Detected License Plate:", license_plate_text.strip())

                        # Store the license plate if no helmet is detected
                        detected_plates.append(license_plate_text.strip())
                        break  # Exit the loop as the license plate is processed

        # Draw bounding boxes
        color = (0, 255, 0) if label == 'Helmet' else (0, 0, 255)
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Show the output frame
    cv2.imshow('Helmet and Motorcycle Detection', frame)

    # Exit loop on 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Print detected license plates for motorcycles without helmets after video ends or user quits
video(video_path)
