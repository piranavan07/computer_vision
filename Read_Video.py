import cv2

capture = cv2.VideoCapture('image\\sample_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # to compress the frames
fps = 30
framesize = (720, 480)

out = cv2.VideoWriter('Sample.avi', fourcc, fps, framesize)

# to read the video frame by frame
while(capture.isOpened()):
    ret, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

out.release()
capture.release()
cv2.destroyAllWindows()