import numpy as np 
import cv2
template=cv2.imread('pentagon.jpg')
target=cv2.imread('shapestomatch.jpg')
cv2.imshow("template",template)
cv2.waitKey(0)
cv2.imshow("target",target)
cv2.waitKey(0)
target_gray=cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
template_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(template_gray,127,255,0)[:2]
ret,thresh2=cv2.threshold(target_gray,127,255,0)[:2]
contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)
template_contour=contours[1]
#the first contour is always the largest white box so get the secnond largest
contours,hierarchy=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
	match=cv2.matchShapes(template_contour,c,1,0.0)
	print(match)
	if match<0.15:
		closest_contour=c
	else:
		closest_contour=[]
cv2.drawContours(target,[closest_contour],-1,(0,255,0),3)
cv2.imshow("output",target)
cv2.waitKey(0)
cv2.destroyAllWindows()