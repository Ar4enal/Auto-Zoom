import cv2
import numpy as np
from features import extract_image_features
from gaze_tf import test_imgs
from rendering import render_gazes_on_image

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

img = cv2.imread('C:/Users/DELL/Desktop/gaze/pc_right1.jpg')
#print(img)

def ex(img):
    img, faces, face_features = extract_image_features(img)
    return test_imgs(img, faces, face_features)

outputs = ex(img)
print(outputs)
render_gazes_on_image(img,outputs,1280,720,12,720)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',1280,720)
cv2.imshow('img',img)
cv2.waitKey (0)
cv2.destroyAllWindows()

