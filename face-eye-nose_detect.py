#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!python3
import cv2
import math
import numpy as np
facesize = 18
faceDis = 21
pi = math.pi
face_detect=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
lefteye_detect=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
righteye_detect=cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
nose_detect=cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
vid=cv2.VideoCapture(0)

while True:
    ret,img=vid.read()
    ret = vid.set(3,640)
    ret = vid.set(4,480)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_detect.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=gray[y:y+h,x:x+h]
        roi_color=img[y:y+h,x:x+h]
        lefteye=lefteye_detect.detectMultiScale(roi_gray,1.3,5)
        righteye=righteye_detect.detectMultiScale(roi_gray,1.3,5)
        noses=nose_detect.detectMultiScale(roi_gray,1.3,3)
        
        
        for(elx,ely,elw,elh) in lefteye:
            
            cv2.rectangle(roi_color,(elx,ely),(elx+elw,ely+elh),(0,255,0),2)
            
            for(erx,ery,erw,erh) in righteye:
            
                cv2.rectangle(roi_color,(erx,ery),(erx+erw,ery+erh),(0,255,255),2)  
            
                dis_le_mid = np.sqrt((x-elx)^2+(y-ely)^2)
                dis_ri_mid = np.sqrt((x+w-erx-erw)^2+(y-ery)^2)
                dis_sub = dis_le_mid - dis_ri_mid
                dis_face_camera = faceDis * 480/h
                
                text1 = str(dis_face_camera)
                text2 = str(dis_le_mid)
                text3 = str(dis_ri_mid)
                text4 = str(dis_sub)
                
                angle_1 = math.atan((x + w/2 -320)/320 * 1)
                angle = (angle_1/2)/pi * 360
                text1 = str(dis_face_camera)
                text2 = str(dis_le_mid)
                text3 = str(dis_ri_mid)
                text4 = str(dis_sub)
                text5 = str(angle)
                
                cv2.putText(img,text1,(400,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)  
                cv2.putText(img,text2,(400,100),cv2.FONT_HERSHEY_PLAIN,2.0,(234,234,234),2)   
                cv2.putText(img,text3,(400,150),cv2.FONT_HERSHEY_PLAIN,2.0,(0,123,0),2) 
                cv2.putText(img,text4,(400,250),cv2.FONT_HERSHEY_PLAIN,2.0,(0,234,234),2) 
                cv2.putText(img,text5,(400,300),cv2.FONT_HERSHEY_PLAIN,2.0,(0,234,234),2) 
        
            #for(nx,ny,nw,nh) in noses:
                
                #cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(255,0,0),2) 
                              
               
           
    cv2.imshow('Face Detector',img)
    k=cv2.waitKey(100) & 0x0ff
    
    
    if k==27:
        break
vid.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




