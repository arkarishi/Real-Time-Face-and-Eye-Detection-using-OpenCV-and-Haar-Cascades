import cv2


# Load Haar cascade classifiers for face and eyes
def load_cascades():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    return face_cascade, eye_cascade


# Initialize webcam
def initialize_camera():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open webcam.")
        exit()
    return cam


# Detect faces and eyes in the frame
def detect_faces_and_eyes(gray_frame, face_cascade, eye_cascade):
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    detections = []
    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        detections.append((x, y, w, h, eyes))
    return detections


# Draw rectangles around detected faces and eyes
def draw_detections(frame, detections):
    for (x, y, w, h, eyes) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
    return frame


# Main function
def main():
    face_cascade, eye_cascade = load_cascades()
    cam = initialize_camera()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detections = detect_faces_and_eyes(gray, face_cascade, eye_cascade)
        frame = draw_detections(frame, detections)

        cv2.imshow('Face and Eye Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
