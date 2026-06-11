# YOLOv8 Real-Time Object Detection

A real-time object detection system using YOLOv8 and OpenCV that detects and classifies objects through a live webcam feed.

## Demo
The system detects multiple objects in real-time including people, furniture, and everyday items with bounding boxes and confidence scores.

## Technologies Used
- Python 3.11
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch

## Features
- Real-time object detection via webcam
- Bounding box visualization with class labels
- Confidence score display
- Supports 80+ object categories (COCO dataset)

## Installation
```bash
pip install ultralytics opencv-python
```

## Usage
```bash
python detect.py
```
Press **q** to quit the detection window.

## Model
Uses YOLOv8n (nano) pretrained on COCO dataset — optimized for real-time performance.

## Author
Pavan Kumar Chanda — AI Master's Student at BTU Cottbus-Senftenberg