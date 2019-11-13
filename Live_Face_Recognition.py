# import the libraries
import os
from datetime import time

import cv2
import face_recognition


# make a list of all the available images
face_cascade = cv2.CascadeClassifier("C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/Res/new.xml")
images = os.listdir('C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/image/images')

# load your image
img_to_be = cv2.imread('C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/image/messi.png')
image_to_be_matched = face_recognition.load_image_file('C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/image/messi.png')
resized_img = cv2.resize(img_to_be, (int(img_to_be.shape[1]/2), int(img_to_be.shape[0]/2)))
cv2.imshow("Original Image", resized_img)
# encoded the loaded image into a feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

# iterate over each image
for image in images:
    # load the image
    loc_img = "C:/Users/pirana/Documents/My_Projects/Python_project/Computer Vision/image/images/" + image
    #resized_img = cv2.resize(loc_img, (600, 600))
    current_image = face_recognition.load_image_file(loc_img)
    cv2.imshow("Matching Images", current_image)
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # match your image with the image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # check if it was a match

    if result[0]:
        cv2.putText(resized_img, "Match Found", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2, cv2.LINE_AA)
        print("Matched: " + image)
    else:
        cv2.putText(resized_img, "No Match Found", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2, cv2.LINE_AA)
        print("Not matched: " + image)
        cv2.waitKey(0)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
