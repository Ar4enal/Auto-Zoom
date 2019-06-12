import cv2
import numpy as np
import tensorflow as tf
from features import extract_image_features,draw_detected_features

img = cv2.imread('C:/Users/DELL/Desktop/gaze/pc_front2.jpg')
#img = cv2.imread('E:/toolbox/presence-master/notebooks/photos/IMG-1036.JPG')
#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#cv2.imshow("img",img)

img, faces, face_features = extract_image_features(img)
for i, face in enumerate(faces):
    [x, y, w, h] = face
    eyes, face_grid = face_features[i]
    #print(face)
    #print(eyes[0],eyes[1])
    image_face = img[y:y+h,x:x+w]
    image_face = cv2.resize(image_face,(64,64),interpolation = cv2.INTER_CUBIC)
    cv2.imshow("face",image_face)
    [re_x,re_y,re_w,re_h] = eyes[0]
    [le_x,le_y,le_w,le_h] = eyes[1]
    rymin = re_y
    rymax = re_y+re_h
    rxmin = re_x
    rxmax = re_x+re_w
    r_eye = img[rymin:rymax,rxmin:rxmax]
    r_eye = cv2.resize(r_eye,(64,64),interpolation = cv2.INTER_CUBIC)
    #cv2.namedWindow('righteye', cv2.WINDOW_NORMAL)
    cv2.imshow("righteye",r_eye)
    #print(r_eye)
    
    lymin = le_y
    lymax = le_y+le_h
    lxmin = le_x
    lxmax = le_x+le_w
    l_eye = img[lymin:lymax,lxmin:lxmax]
    #cv2.namedWindow('lefteye', cv2.WINDOW_NORMAL)
    l_eye = cv2.resize(l_eye,(64,64),interpolation = cv2.INTER_CUBIC)
    cv2.imshow("lefteye",l_eye)

    #to_p = np.copy(face_grid)
    #face_mask = np.copy(to_p).reshape(25,25)
    #print(face_mask)



draw_detected_features(img,faces,face_features)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow("img",img)
cv2.waitKey (0)
cv2.destroyAllWindows()