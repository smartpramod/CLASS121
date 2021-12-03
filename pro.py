
import cv2
import time
import numpy as np

#Starting the webcam
video = cv2.VideoCapture(0)
image = cv2.imread("C121p.jpg")

while True:
    #ret is returning and frame saves the captures.
    ret, frame = video.read()
    print(frame)

    #Resize the image of our and the frame of our video
    image = cv2.resize(image,(640,480))
    frame = cv2.resize(frame,(640,480))

    #Range of our making color
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    #Setting the range
    mask = cv2.inRange(frame,l_black,u_black)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    f = frame - res
    f = np.where(f == 0,image,f)
    
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    # Listen for ESC or q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()