'''import numpy as np
import cv2
cap=cv2.VideoCapture("highway.mp4")
ret,first_frame=cap.read()
first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray=cv2.GaussianBlur(first_gray,(5,5),0)
while True:
	ret,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray_frame=cv2.GaussianBlur(gray_frame,(5,5),0)
	difference=cv2.absdiff(first_gray,gray_frame)
	ret,difference=cv2.threshold(difference,25,255,cv2.THRESH_BINARY)
 	#cv2.imshow("Frame",frame)
	cv2.imshow("First Frame",first_frame)
	cv2.imshow("difference",difference)
	key=cv2.waitKey(25)
	#the higher the number inside waitKey the slower will be the motion
	if key == 13:
		break
cap.release()
cv2.destroyAllWindows()
'''
##////////////////////////////////
#this program is itself capable of doing background subtraction but it 
#is not that efficient becoz from frame subtraction u would have to actually 
#wait for a particular point where the frame is such that it has no cars and 
#hence that is the ideal frame
'''import numpy as np
import cv2
cap=cv2.VideoCapture("highway.mp4")
subtractor=cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=25,detectShadows=False)
#this function removes noise automatically
#also it uses many filters including morphological to make a good frame to be subtracted
while True:
	ret,frame=cap.read()
	mask=subtractor.apply(frame)
	cv2.imshow("Frame",frame)
	cv2.imshow("Mask",mask)
	key=cv2.waitKey(30)
	if key == 13:
		break
cap.release()
cv2.destroyAllWindows()
'''
#this above functioin is now a better background subtraction than the previous one
#now the below function is of live backgroung subtraction
import numpy as np
import cv2
cap=cv2.VideoCapture(0)
subtractor=cv2.createBackgroundSubtractorMOG2()
#this function removes noise automatically
#also it uses many filters including morphological to make a good frame to be subtracted
while True:
	ret,frame=cap.read()
	mask=subtractor.apply(frame)
	cv2.imshow("Frame",frame)
	cv2.imshow("Mask",mask)
	key=cv2.waitKey(30)
	if key == 13:
		break
cap.release()
cv2.destroyAllWindows()