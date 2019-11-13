import cv2

pic = cv2.imread('image\\face.jpg')
matrix = (7, 7)

# GaussianBlur
G_blur = cv2.GaussianBlur(pic, matrix, 0)


# median blur  used to remove noise
kernal = 3
M_blur = cv2.medianBlur(pic, kernal)

cv2.imshow('Original', pic)
cv2.imshow('Median Blur', M_blur)
cv2.imshow('Gaussian Blur', G_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

