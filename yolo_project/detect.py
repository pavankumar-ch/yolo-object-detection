import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open webcam
cap = cv2.VideoCapture(0)

print("Starting real-time object detection... Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection
    results = model(frame)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow('YOLOv8 Real-Time Object Detection', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Detection stopped.")