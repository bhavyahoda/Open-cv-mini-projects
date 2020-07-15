def top_lip(landmarks):
	top_lip_pts=[]
	for i in range(49,55):
		top_lip_pts.append(landmarks[i])
	for i in range(61,64):
		top_lip_pts.append(landmarks[i])
	top_lip_all_pts=np.squeeze(np.asarray(top_lip_pts))
	top_lip_mean=np.mean(top_lip_pts,axis=0)
	return int(top_lip_mean[:,1])
def bottom_lip(landmarks):
	bottom_lip_pts=[]
	for i in range(65,68):
		bottom_lip_pts.append(landmarks[i])
	for i in range(55,60):
		bottom_lip_pts.append(landmarks[i])
	bottom_lip_all_pts=np.squeeze(np.array(bottom_lip_pts))
	bottom_lip_mean=np.mean(bottom_lip_pts,axis=0)
	return int(bottom_lip_mean[:,1])
