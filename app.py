import cv2
import numpy as np

'''
# basics 

img = cv2.imread('image//messi.jpg', 1)
img = cv2.imwrite('image//messi1.png', img) # for convert new type
#cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# Drawing
'''
Define the dimention of the image Create the image with numpy arrays Create black background
by filling the arrays with Zeros

Implement drawing function

#500x500 pixel with 3 dimention dtype= 8bit unasigned int
pic = np.zeros((500, 500, 3), dtype='uint8')

    # diagonal x,y 2 cominations first and color , channel linetype .. or _
#cv2.rectangle(pic, (0, 0), (500, 150), (255, 255, 255), 3, lineType=8, shift=0)

    # to draw line
#cv2.line(pic, (350, 350), (500, 350), (0, 0, 255))

color = (255, 0, 255)
    # to draw circle x,y cor , radius, color
#cv2.circle(pic, (250, 250), 75, color)

    # to draw text import font variable
font = cv2.FONT_HERSHEY_DUPLEX
    # to draw text , text, starting cordinates, font, size of text, color, thickness, line type
cv2.putText(pic, 'Pirana', (100, 100), font, 3, (255, 0, 255), 4, cv2.LINE_8)

    #drawing combination or image
pic = np.zeros((500, 500, 3), dtype='uint8')
cv2.rectangle(pic, (0, 0), (500, 150), (123, 200, 98), 3, lineType=8, shift=0)
cv2.putText(pic, 'Pirana', (100, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 4, cv2.LINE_8)
cv2.circle(pic, (250, 250), 50, (255, 0, 255))
cv2.line(pic, (133, 138), (388, 133), (0, 0, 255))

cv2.imshow('Dark', pic)
cv2.imwrite('test.jpg', pic)


# Image transformation

pic = cv2.imread('image\\face.jpg')
cols = pic.shape[1]
rows = pic.shape[0]

    # shift 150 right and 70 down
#M = np.float32([[1, 0, 150], [0, 1, 70]])
M = np.float32([[1, 0, -150], [0, 1, -70]]) # side change
    #shifting
shifted = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('Shifted', shifted)
'''
# image rotation
pic = cv2.imread('image\\face.jpg')
cols = pic.shape[1]
rows = pic.shape[0]
center = (cols/2, rows/2)
angle = -90

M = cv2.getRotationMatrix2D(center, angle, 1)

rotate = cv2.warpAffine(pic, M, (cols, rows))

cv2.imshow('Rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
