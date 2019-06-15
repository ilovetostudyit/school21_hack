import argparse

import cv2
import numpy as np
import os, sys

refPt = []
cropping = False
calibrate = True

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping, calibrate
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if calibrate == True:
		if event == cv2.EVENT_LBUTTONDOWN:
			refPt = [(x, y)]
			cropping = True
	
		# check to see if the left mouse button was released
		elif event == cv2.EVENT_LBUTTONUP:
			# record the ending (x, y) coordinates and indicate that
			# the cropping operation is finished
			refPt.append((x, y))
			cropping = False
			calibrate = False

cap = cv2.VideoCapture(0)
a = 0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imshow("frame",frame)
	clone = frame.copy()
	cv2.namedWindow("frame")
	cv2.setMouseCallback("frame", click_and_crop)
	key = cv2.waitKey(1) & 0xFF
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		frame = clone.copy()
		cv2.imshow("frame", frame)
		refPt = []
		calibrate = True
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
	elif key == ord("s") and cropping == False:
		cv2.imwrite( "images/ROI" + str(a) +".jpg", roi)
		a = a + 1
	elif key == ord("d"):
		folder = 'images'
		for the_file in os.listdir(folder):
			file_path = os.path.join(folder, the_file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
			except Exception as e:
				print(e)
	if len(refPt) == 2:
		roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
		cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("frame",frame)
		cv2.imshow("ROI", roi)
		#cv2.waitKey(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
