import argparse

import cv2
import numpy as np

refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping, image
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
 
		# draw a rectangle around the region of interest
        image = frame.copy()
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow("frame",frame)
    clone = frame.copy()
    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame", click_and_crop)
    key = cv2.waitKey(1) & 0xFF
	# if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
	    image = clone.copy()
	# if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
	    break
    if len(refPt) == 2:
	    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	    cv2.imshow("ROI", roi)
	    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# import the necessary packages
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
 

 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
