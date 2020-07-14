def get_landmarks(img):
	rects=detector(img,1)
	if len(rects)>1:
		return "error"
	if len(rects)== 0:
		return "error"
	return np.matrix([[p.x,p.y] for p in predictor(img,rects[0]).parts()])
def annonate_landmarks(img,landmarks):
	img=img.copy()
	for idx,point in enumerate(landmarks):
		pos=(point[0,0],point[0,1])
		cv2.putText(img,str(idx),pos,fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,255))
		cv2.circle(img,pos,3,color=(0,255,255))
	return img