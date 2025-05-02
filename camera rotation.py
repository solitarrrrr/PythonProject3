import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    y,x,z=frame.shape

    frame_resized=cv2.resize(frame,(int(x/2),int(y/2)))

    output=np.zeros((y,x,z),'unit8')
    output[0:int(y/2),0:int(x/2)]=frame_resized
    output_1=cv2.flip(frame_resized,1)
    output[0:int(y/2),int(x/2):x]=output_1
    output_2=cv2.flip(frame_resized,0)
    output[int(y/2):y,0:int(x/2)]= output_2
    output_3=cv2.flip(frame_resized,-1)
    output[int(y/2):y,int(x/2):x]=output_3

    cv2.imshow('python',frame)

    if cv2.waitKey(1)==ord('a'):
        breakcap.release()
        cv2.destroyAllWindows()


