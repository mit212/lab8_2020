import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Changes image to gray

    # Display the resulting frame
    reg = cv2.imshow('frame', frame)
    grayframe = cv2.imshow('gray', gray) #shows the gray image

    if cv2.waitKey(1) & 0xFF == ord('q'):  #press the lowercase q button to quit
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()