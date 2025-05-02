import cv2
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    faces = face_cascade.detectMultiScale(frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)        # ( (B,G,R), (width))
    cv2.imshow('facedetection', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
