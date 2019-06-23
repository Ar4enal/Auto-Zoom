通过cap.get(propld)访问视频的某些功能，propld是0到18之间的数字。每个数字表示视频的属性。
比如：
cap.get（cv2.CAP_PROP_FRAME_WIDTH）和cap.get（cv2.CAP_PROP_FRAME_HEIGHT）得到帧宽和高度.
如果想修改为320x240.只需使用
ret = cap.set（cv2.CAP_PROP_FRAME_WIDTH，320）和
ret = cap.set（cv2.CAP_PROP_FRAME_HEIGHT，240）.

参数	propld	功能
cv2.CAP_PROP_POS_MSEC	      0	    视频文件的当前位置（以毫秒为单位）或视频捕获时间戳
cv2.CAP_PROP_POS_FRAMES	      1	    基于0的索引将被解码/捕获下一帧
cv2.CAP_PROP_POS_AVI_RATIO	  2	    视频文件的相对位置：0 - 视频的开始，1 - 视频的结束
cv2.CAP_PROP_FRAME_WIDTH	  3	    帧的宽度
cv2.CAP_PROP_FRAME_HEIGHT	  4	    帧的高度
cv2.CAP_PROP_FPS	          5	    帧速
cv2.CAP_PROP_FOURCC	          6	    4个字符表示的视频编码器格式
cv2.CAP_PROP_FRAME_COUNT	  7	    帧数
cv2.CAP_PROP_FORMAT	          8	    byretrieve()返回的Mat对象的格式
cv2.CAP_PROP_MODE	          9	    指示当前捕获模式的后端特定值
cv2.CAP_PROP_BRIGHTNESS	      10    图像的亮度（仅适用于相机）
cv2.CAP_PROP_CONTRAST	      11    图像对比度（仅适用于相机）
cv2.CAP_PROP_SATURATION	      12	图像的饱和度（仅适用于相机）
cv2.CAP_PROP_HUE	          13	图像的色相（仅适用于相机）
cv2.CAP_PROP_GAIN	          14	图像的增益（仅适用于相机）
cv2.CAP_PROP_EXPOSURE	      15	曝光（仅适用于相机）
cv2.CAP_PROP_CONVERT_RGB	  16	表示图像是否应转换为RGB的布尔标志
cv2.CAP_PROP_WHITE_BALANCE	  17	
cv2.CAP_PROP_RECTIFICATION	  18	立体摄像机的整流标志