import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(4,360)
cap.set(5,240)
cap.set(6,30)
def callback(x):
	pass
cv2.namedWindow('input')
lowH = 0;highH = 179
lowV = 0;highV = 255
lowS = 0;highS = 255
cv2.createTrackbar('lowH','input',lowH,179,callback)
cv2.createTrackbar('highH','input',highH,179,callback)
cv2.createTrackbar('lowV','input',lowV,255,callback)
cv2.createTrackbar('highV','input',highV,255,callback)
cv2.createTrackbar('lowS','input',lowS,255,callback)
cv2.createTrackbar('highS','input',highS,255,callback)
while(True):
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lowH = cv2.getTrackbarPos('lowH','input')
	highH = cv2.getTrackbarPos('highH','input')
	lowS= cv2.getTrackbarPos('lowS','input')
	highS = cv2.getTrackbarPos('highS','input')
	lowV = cv2.getTrackbarPos('lowV','input')
	highV = cv2.getTrackbarPos('highV','input')	
	high = np.array([highH,highS,highV])
	low = np.array([lowH,lowS,lowV])
	mask = cv2.inRange(hsv, low, high)
	_,th = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
	i,contours,h= cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	#print(len(contours))
	for cnt in contours:
		# app = cv2.approxPolyDP(cnt,0.04*cv2.arcLength(cnt,True),True)
		# if len(app) >= 4 and len(app) <= 6:
		# 	show =cv2.drawContours(frame,[cnt],0,(0,0,255),3)
		# 	cv2.imshow('sh',show)
		area = cv2.contourArea(cnt)
		if 400 <= area <= 2000:
			show = cv2.drawContours(frame, [cnt],0,(0,0,255),3)
			cv2.imshow('sh',show)
	res = cv2.bitwise_and(frame,frame,mask = mask)
	cv2.imshow('mask', th)
	cv2.imshow('input',frame)
	cv2.imshow('Detected', res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllwindows()