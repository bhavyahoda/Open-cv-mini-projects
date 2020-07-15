import numpy as np
import cv2
import dlib
PREDICTOR_PATH="shape_predictor_68_face_landmarks.dat"
predictor=dlib.shape_predictor(PREDICTOR_PATH)
detector=dlib.get_frontal_face_detector()
def mouth_open(img):
	landmarks=get_landmarks(img)
	if landmarks=="error":
		return img,0
	img_with_landmarks=annonate_landmarks(img,landmarks)
	top_lip_center=top_lip(landmarks)
	bottom_lip_center=bottom_lip(landmarks)
	lip_distance=abs(top_lip_center-bottom_lip_center)
	return img_with_landmarks,lip_distance

cap=cv2.VideoCapture(0)
yawns=0
yawn_status=False
while True:
	ret,frame=cap.read()
	img_landmarks,lip_distance=mouth_open(frame)
	prev_yawn_status=yawn_status
	if lip_distance>20:
		yawn_status=True
		cv2.putText(frame,"subject is yawning",(50,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
		output_text="Yawn count:"+str(yawns+1)
		cv2.putText(frame,output_text,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,127),2)
	else:
		yawn_status=False
	if prev_yawn_status==True and yawn_status==False:
		yawns+=1
	#cv2.imshow("live landmark",img_landmarks)
	cv2.imshow("yawn detection ",frame)
	if cv2.waitKey(1) == 13 :
		break
cap.release()
cv2.destroyAllWindows()
