ͨ��cap.get(propld)������Ƶ��ĳЩ���ܣ�propld��0��18֮������֡�ÿ�����ֱ�ʾ��Ƶ�����ԡ�
���磺
cap.get��cv2.CAP_PROP_FRAME_WIDTH����cap.get��cv2.CAP_PROP_FRAME_HEIGHT���õ�֡��͸߶�.
������޸�Ϊ320x240.ֻ��ʹ��
ret = cap.set��cv2.CAP_PROP_FRAME_WIDTH��320����
ret = cap.set��cv2.CAP_PROP_FRAME_HEIGHT��240��.

����	propld	����
cv2.CAP_PROP_POS_MSEC	      0	    ��Ƶ�ļ��ĵ�ǰλ�ã��Ժ���Ϊ��λ������Ƶ����ʱ���
cv2.CAP_PROP_POS_FRAMES	      1	    ����0��������������/������һ֡
cv2.CAP_PROP_POS_AVI_RATIO	  2	    ��Ƶ�ļ������λ�ã�0 - ��Ƶ�Ŀ�ʼ��1 - ��Ƶ�Ľ���
cv2.CAP_PROP_FRAME_WIDTH	  3	    ֡�Ŀ��
cv2.CAP_PROP_FRAME_HEIGHT	  4	    ֡�ĸ߶�
cv2.CAP_PROP_FPS	          5	    ֡��
cv2.CAP_PROP_FOURCC	          6	    4���ַ���ʾ����Ƶ��������ʽ
cv2.CAP_PROP_FRAME_COUNT	  7	    ֡��
cv2.CAP_PROP_FORMAT	          8	    byretrieve()���ص�Mat����ĸ�ʽ
cv2.CAP_PROP_MODE	          9	    ָʾ��ǰ����ģʽ�ĺ���ض�ֵ
cv2.CAP_PROP_BRIGHTNESS	      10    ͼ������ȣ��������������
cv2.CAP_PROP_CONTRAST	      11    ͼ��Աȶȣ��������������
cv2.CAP_PROP_SATURATION	      12	ͼ��ı��Ͷȣ��������������
cv2.CAP_PROP_HUE	          13	ͼ���ɫ�ࣨ�������������
cv2.CAP_PROP_GAIN	          14	ͼ������棨�������������
cv2.CAP_PROP_EXPOSURE	      15	�ع⣨�������������
cv2.CAP_PROP_CONVERT_RGB	  16	��ʾͼ���Ƿ�Ӧת��ΪRGB�Ĳ�����־
cv2.CAP_PROP_WHITE_BALANCE	  17	
cv2.CAP_PROP_RECTIFICATION	  18	�����������������־