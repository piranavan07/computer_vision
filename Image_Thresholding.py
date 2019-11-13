import cv2

pic = cv2.imread('image\\face.jpg', 0)
threshold_value = 100

(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY) #inverse THRESH_BINARY_INV

cv2.imshow('Binary', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
