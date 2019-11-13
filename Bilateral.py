import cv2

pic = cv2.imread('image\\face.jpg', 1)

dimpixel = 7  # center round
color = 100
space = 100
filter = cv2.bilateralFilter(pic, dimpixel, color, space)

cv2.imshow('Bilateral', filter)
cv2.waitKey(0)
cv2.destroyAllWindows()