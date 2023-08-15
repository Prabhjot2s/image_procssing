import cv2
import time

Video=cv2.VideoCapture(0)
time.sleep(1)
first_frame=None
second_frame=None
rectangle=None
while True:

    check, frame=Video.read()
    grey_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_scale_gau=cv2.GaussianBlur(grey_scale,(21,21),0)

    if first_frame is None:
        first_frame=gray_scale_gau
    delta=cv2.absdiff(first_frame,gray_scale_gau)

    thrsh_frame=cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]
    dil_frame=cv2.dilate(thrsh_frame,None,iterations=2)

    counters,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for counter in counters:
        if cv2.contourArea(counter) < 30000:
            continue
        x,y,w,h=cv2.boundingRect(counter)
        rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    if second_frame is None:
        second_frame=rectangle


    cv2.imshow("video",frame)


    key=cv2.waitKey(1)
    if key==ord('q'):
        break

Video.release()
cv2.imwrite('imag.png',second_frame)