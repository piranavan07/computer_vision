import cv2
import pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

print(datetime.now())
while True:
    check, frame = video.read()
    status = 0
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #coverting to gray scale
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)  #coverting the gray scale into Gaussian blur

    if first_frame is None:  #to store first frame
        first_frame = gray_img
        continue
delta_frame = cv2.absdiff(first_frame, gray_img)   #calculating diff between first and current frame
thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]  #if diff value <30 to black else white
thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

(_, cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #add the border

for contour in cnts:      # remove noises and shadow and make >1000pxl white
    if cv2.contourArea(contour) < 10000:
        continue
    status = 1   # after object detected
    (x, y, w, h) = cv2.boundingRect(contour)  #create rectangle box
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

status_list.append(status)
status_list = status_list[-2:]

if status_list[-1] == 1 and status_list[-2] == 0:
    times.append(datetime.now())
if status_list[-1] == 0 and status_list[-2] == 1:
    times.append(datetime.now())

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)  # store time value in a dataframe

df.to_csv("Times.csv")
cv2.imshow('Frame', frame)
cv2.imshow('Capturing ', gray_img)
cv2.imshow('delta', delta_frame)
cv2.imshow('thresh', thresh_delta)

video.release()
cv2.destroyAllWindow()


