import cv2, time

'''
#for reading color image use 1
img = cv2.imread("C:\\Users\\pirana\\Documents\\My_Projects\\Python_project\\Computer Vision\\image\\Image_128.jpg",1)

#for reading B/W image use 0
img1 = cv2.imread("C:\\Users\\pirana\\Documents\\My_Projects\\Python_project\\Computer Vision\\image\\bigMug.jpg",1)

#resizing image
#resized_img = cv2.resize(img1, (600,600))

#resizing by half size devide by 2 and to get bigger img multiply the shape row and col
resized_img = cv2.resize(img1, (int(img1.shape[1]*2),int(img1.shape[0]*2)))


#this will show how computer reads the img
print(img)

print(type(img1))

print(img1.shape)  # pixel shape


print(img1.shape)
print(resized_img .shape)

# to display the image
cv2.imshow("picture " , img1)
cv2.imshow("picture2" , resized_img)

# if delay as 0 wait for key to enter
cv2.waitKey(0)  # 2000 mili second window automatically close
cv2.destroyAllWindows()
'''
video = cv2.VideoCapture(0)

a = 1

while True:
    a=a+1
    check, frame = video.read()
#print(check)
    print(frame)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("capture", gray_img)
    #cv2.imshow('captureing' , frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
time.sleep(3)
