import cv2

# showing the edges around the image its like drawing effect
pic = cv2.imread('image\\face.jpg')

threshold_value1 = 50
threshold_value2 = 150

canny = cv2.Canny(pic, threshold_value1, threshold_value2)

cv2.imshow('canny pic', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()