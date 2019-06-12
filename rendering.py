import cv2
import numpy as np
import matplotlib.pyplot as plt



def render_gazes_on_image(frame, outputs, window_width, window_height, window_height_cm, camera_h_from_screen_top):

    pixels_per_cm = window_height * 1. / window_height_cm
    h, w, c = frame.shape
    #print(window_height, window_height_cm)
    alphaReserve = 0.8
    BChannel = 0
    GChannel = 255
    RChannel = 0

    camera_pixels_from_l = window_width / 2
    #camera_pixels_from_top = camera_h_from_screen_top * pixels_per_cm
    camera_pixels_from_top = camera_h_from_screen_top/ 2

    x_translation_from_camera_c = camera_pixels_from_l
    y_translation_from_camera_c = camera_pixels_from_top

    #print(pixels_per_cm, x_translation_from_camera_c, y_translation_from_camera_c)
    #print(outputs)
    if not outputs:
        return frame
    for output in outputs:

        screen_x = output[0,0] * pixels_per_cm + x_translation_from_camera_c 
        screen_y = -output[0,1] * pixels_per_cm + y_translation_from_camera_c

        print("in px:", round(screen_x), round(screen_y))

        if screen_x >= 920 and screen_y >= 350:
            #  cv2.circle(frame, (20, 20), 5, (0, 0, 255), -1)
            #cv2.circle(frame, (int(round(screen_x)),int(round(screen_y))), 5, (0, 0, 255), -1)
            print('↘ bottom right corner')
            yMin = h//2
            yMax = h
            xMin = w//2
            xMax = w

            frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)

        elif screen_x >=920 and screen_y <= 350:
            print('↗ upper right corner')
            yMin = 0
            yMax = h//2
            xMin = w//2
            xMax = w

            frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
        elif screen_x <=920 and screen_y >= 350:
            print('↙ bottom left corner')
            yMin = h//2
            yMax = h
            xMin = 0
            xMax = w//2

            frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
        elif screen_x <=920 and screen_y <= 350:
            print('↖ upper left corner')
            yMin = 0
            yMax = h//2
            xMin = 0
            xMax = w//2

            frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
        else:
            print('㊣')
            yMin = h//4
            yMax = h*3//4
            xMin = w//4
            xMax = w*3//4

            frame[yMin:yMax, xMin:xMax, 0] = frame[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 1] = frame[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
            frame[yMin:yMax, xMin:xMax, 2] = frame[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
    return frame
    """        
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img',1280,720)
    cv2.imshow('img',frame)
    cv2.waitKey (0)
    cv2.destroyAllWindows()
    """

