import numpy as np
import cv2

video_path = "/Users/jeff/Downloads/videoplayback.mp4"
output_path = "/Users/jeff/Downloads/testvideo/"
cap = cv2.VideoCapture(video_path)

i = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    cv2.imwrite(output_path+str(i)+".png", frame)
    i = i + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()