# Image face detection
import cv2

face_cascade = cv2.CascadeClassifier('Res\\haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
scale_factor = 1.3

while 1:
    ret, pic = video_capture.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(pic, (x, y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic, 'pirana', (x, y), font, 2, (255, 0, 255), 2, cv2.LINE_AA)

    print("Number of faces found {} ".format(len(faces)))
    cv2.imshow('Face', pic)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
