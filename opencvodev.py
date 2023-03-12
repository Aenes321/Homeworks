import cv2 as cv
import numpy as np
def nothing(x):
    pass
cap=cv.VideoCapture('reddetection.mp4')
#cap=cv.VideoCapture(0)
#cv.namedWindow("tracking")
#cv.createTrackbar('LH','tracking',38,255,nothing)
#cv.createTrackbar('LS','tracking',75,255,nothing)
#cv.createTrackbar('LV','tracking',134,255,nothing)
#cv.createTrackbar('UH','tracking',184,255,nothing)
#cv.createTrackbar('US','tracking',180,255,nothing)
#cv.createTrackbar('UV','tracking',255,255,nothing)
while cap.isOpened():
    _,frame=cap.read()
    middley=int(frame.shape[0]/2)
    middlex=int(frame.shape[1]/2)

    gauss=cv.GaussianBlur(frame,(9,9),0)

    gaussgray=cv.cvtColor(gauss,cv.COLOR_BGR2GRAY)

    hsv2=cv.cvtColor(gauss,cv.COLOR_BGR2HSV)
 
    contours1,_=cv.findContours(gaussgray,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

#    l_h=cv.getTrackbarPos('LH','tracking')
#    l_s=cv.getTrackbarPos('LS','tracking')
#    l_v=cv.getTrackbarPos('LV','tracking')

#    u_h=cv.getTrackbarPos('UH','tracking')
#    u_s=cv.getTrackbarPos('US','tracking')
#    u_v=cv.getTrackbarPos('UV','tracking')

#    l_b=np.array([l_h,l_s,l_v])
#    u_b=np.array([u_h,u_s,u_v])
    l_b=np.array([38,75,134])
    u_b=np.array([184,180,255])


    mask1=cv.inRange(hsv2,l_b,u_b)

    res1=cv.bitwise_and(gaussgray,gaussgray,mask=mask1)

    contours1,_=cv.findContours(res1,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

    for contour in contours1:
        approx=cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
        (x,y,w,h)=cv.boundingRect(contour)
        A=middlex-(x+40)
        B=middley-(y+40)
        C=(A**2+B**2)**0.5
        distance=round(C,1)
        if cv.contourArea(contour)<500:
            continue
        cv.drawContours(frame,[approx],0,(0,255,0),5)
        cv.line(frame,(x+40,y+40),(middlex,middley),(255,0,0),2)
        cv.putText(frame,'Distance:{}'.format(distance),(20,30),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)


    cv.imshow('frame',frame)

    
    key=cv.waitKey(20)
    if key==27:
        break
cap.release()