import cv2
 
# create a new cam object
cap = cv2.VideoCapture(0)
# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier("C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/Res/new.xml")
while True:
    # read the image from the cam
    ret, image = cap.read()
    # converting to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect all the faces in the image
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.05, minNeighbors=5)

    no_faces = "Number of face(s) found {} ".format(len(faces))
    print(no_faces)
    # for every face, draw a blue rectangle
    cv2.imshow("image", image_gray)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
        cv2.putText(image, no_faces, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("image", image)
    print(image.shape)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
