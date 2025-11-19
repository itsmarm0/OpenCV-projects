# Color Detection with OpenCV
This project demonstrates **real-time color detection** using OpenCV and Python.  
It captures video from your webcam, converts frames to HSV color space, and detects a target color by drawing a bounding box around it.

## Features
- Real-time webcam feed
- HSV color masking
- Bounding box detection using `PIL.Image.getbbox()`
- Easily extendable to multiple colors and shapes

## Requirements
1) Python 3.x
2) OpenCV (`pip install opencv-python`)
3) NumPy (`pip install numpy`)
4) Pillow (`pip install pillow`)

How It Works:
Capture frames from webcam using cv2.VideoCapture.
Convert frames to HSV color space.
Apply a mask using lower/upper HSV limits (get_limits()).
Convert mask to a PIL image and extract bounding box.
Draw a rectangle around detected color region.
