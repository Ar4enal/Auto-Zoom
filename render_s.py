import cv2
import numpy as np

def detect_gaze(frame, outputs, window_width, window_height, window_height_cm, camera_h_from_screen_top):
    pixels_per_cm = window_height * 1. / window_height_cm
    camera_pixels_from_l = window_width / 2
    camera_pixels_from_top = camera_h_from_screen_top/ 2

    x_translation_from_camera_c = camera_pixels_from_l
    y_translation_from_camera_c = camera_pixels_from_top

    gaze=0

    if not outputs:
        gaze = 0
        return gaze
    for output in outputs:

        screen_x = output[0,0] * pixels_per_cm + x_translation_from_camera_c 
        screen_y = -output[0,1] * pixels_per_cm + y_translation_from_camera_c

        #print("in px:", round(screen_x), round(screen_y))
        if screen_x == 640 and screen_y == 360:
            print('zheng')
            gaze=0
            break
        if screen_x >= 915 and screen_y >= 350:
            print('bottom right corner')
            gaze=1

        elif screen_x >=915 and screen_y <= 350:
            print('upper right corner')
            gaze=2

        elif screen_x <=915 and screen_y >= 350:
            print('bottom left corner')
            gaze=3

        elif screen_x <=915 and screen_y <= 350:
            print('upper left corner')
            gaze=4
            
    return gaze

def draw_gaze(frame,gaze):
    
    h, w, c = frame.shape
    alphaReserve = 0.8
    BChannel = 0
    GChannel = 0
    RChannel = 255

    if gaze==0:
        """
        yMin = h//4
        yMax = h*3//4
        xMin = w//4
        xMax = w*3//4

        frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)  
        """
        return frame
    elif gaze==1:
        yMin = h//2
        yMax = h
        xMin = w//2
        xMax = w

        frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    elif gaze==2:
        yMin = 0
        yMax = h//2
        xMin = w//2
        xMax = w

        frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    elif gaze==3:
        yMin = h//2
        yMax = h
        xMin = 0
        xMax = w//2

        frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    elif gaze==4:
        yMin = 0
        yMax = h//2
        xMin = 0
        xMax = w//2

        frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
        frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    
    return frame


