import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore")
from rendering import render_gazes_on_image
from features import extract_image_features
from gaze_tf import test_imgs

window_width = 1280
window_height = 720

def show_gaze(img):
    img, faces, face_features = extract_image_features(img)
    return test_imgs(img, faces, face_features)

class GazeDetectStream:
    def __init__(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,1280)
        cap.set(4,720)
        cap.set(11, 0.1)
        cap.set(15, 0.01)
        cap.set(cv2.CAP_PROP_FRAME_COUNT, 1)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        cap.set(6, 1)
        self.is_first_frame = True
        self.cap = cap

    def __iter__(self):
        return self

    def __next__(self):
        ret, frame = self.cap.read()
        outputs = show_gaze(frame)
        #print(outputs)
        return frame, outputs

for frame,outputs in GazeDetectStream():
    result = render_gazes_on_image(frame,outputs,1280,720,12,720)
    cv2.imshow('result',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

