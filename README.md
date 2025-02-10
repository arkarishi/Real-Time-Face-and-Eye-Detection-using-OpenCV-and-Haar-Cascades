# Real-Time-Face-and-Eye-Detection-using-OpenCV-and-Haar-Cascades
This project implements real-time face and eye detection using OpenCV's Haar cascade classifiers. The program captures video from a webcam, detects faces and eyes, and visualizes them with bounding boxes.

Features
Real-time face and eye detection
Uses OpenCV's Haar cascade classifiers
Highlights detected faces in blue and eyes in green
Works with live webcam feed

Prerequisites
Ensure you have Python installed along with the required dependencies:
pip install opencv-python

Usage
Clone the repository or copy the script.
Run the Python script:
python face_eye_detection.py
The webcam window will open, showing real-time face and eye tracking.
Press q to exit the application.

Code Explanation
Loads Haar cascade classifiers for face and eye detection.
Captures video frames from the webcam.
Converts frames to grayscale for better detection performance.
Detects faces and eyes, then draws bounding boxes around them.
Displays the processed frame in real-time.

Key Libraries Used
OpenCV: For video capture, image processing, and Haar cascade-based face and eye detection.
