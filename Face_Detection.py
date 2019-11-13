import cv2

#create a cascade classifier object
face_cascade = cv2.CascadeClassifier("C:\\Users\\pirana\\Documents\\My_Projects\\Python_project\\Computer Vision\\"
                                     "Res\\new.xml")
#eye_cascade = cv2.CascadeClassifier("C:\\Users\\pirana\\Documents\\My_Projects\\Python_project\\Computer Vision\\"
#                                       "haarcascades\\haarcascade_eye.xml")

img = cv2.imread("C:\\Users\\pirana\\Documents\\My_Projects\\Python_project\\Computer Vision\\image\\face.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search for the face co-ordinates

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
