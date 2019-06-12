import tensorflow as tf
import numpy as np
from lib import current_time, crop_image
import os
import scipy.io
import cv2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model_dir = os.path.dirname(os.path.realpath(__file__)) + "/GazeCapture/models/itracker_tf"

image_size = 64

sess = tf.Session()

saver = tf.train.import_meta_graph(model_dir+'/model-23.meta')
saver.restore(sess,tf.train.latest_checkpoint(model_dir))

graph = tf.get_default_graph()
a = graph.get_tensor_by_name("eye_left:0")
b = graph.get_tensor_by_name("eye_right:0")
c = graph.get_tensor_by_name("face:0")
d = graph.get_tensor_by_name("face_mask:0")
#e = graph.get_tensor_by_name("pos:0")
e = graph.get_tensor_by_name("Add_5:0")
#e = graph.get_tensor_by_name("fc2_w:0")
#e = graph.get_tensor_by_name("Variable_13:0")
#e = tf.get_collection("validation_nodes")
#y = tf.placeholder(tf.float32, [None, 2], name='pred')
print('Successfully load the trained model!')
#print(e)

def test_img(img,face,face_feature):
    if not face_feature:
        return None
    #sess = tf.Session()
    #init = tf.global_variables_initializer()
    #sess.run(init)
    eyes, face_grid = face_feature
    [x, y, w, h] = face
    if len(eyes) < 2:
        g = np.array([[0,0]])
        return g
    start_ms = current_time()

    [re_x,re_y,re_w,re_h] = eyes[0]
    [le_x,le_y,le_w,le_h] = eyes[1]
    rymin = re_y
    rymax = re_y+re_h
    rxmin = re_x
    rxmax = re_x+re_w
    r_eye = img[rymin:rymax,rxmin:rxmax]
    r_eye = cv2.resize(r_eye,(64,64),interpolation = cv2.INTER_CUBIC)
    lymin = le_y
    lymax = le_y+le_h
    lxmin = le_x
    lxmax = le_x+le_w
    l_eye = img[lymin:lymax,lxmin:lxmax]
    l_eye = cv2.resize(l_eye,(64,64),interpolation = cv2.INTER_CUBIC)
    
    image_face = img[y:y+h,x:x+w]
    image_face = cv2.resize(image_face,(64,64),interpolation = cv2.INTER_CUBIC)

    transformed_left_eye = l_eye/255
    transformed_right_eye = r_eye/255
    transformed_face = image_face/255
    transformed_face_grid = face_grid

    #print(transformed_face_grid)
    
    transformed_left_eye = np.expand_dims(transformed_left_eye,0)
    transformed_right_eye = np.expand_dims(transformed_right_eye,0)
    transformed_face = np.expand_dims(transformed_face,0)
    transformed_face_grid = np.expand_dims(transformed_face_grid,0)

    feed_dict = {a:transformed_left_eye, b:transformed_right_eye, c:transformed_face, d:transformed_face_grid}

    res = sess.run(e,feed_dict)
    print("Feeding through the network took " + str((current_time() - start_ms) * 1. / 1000) + "s")
    #res = res*(-255)
    #res = res.astype('int')
    return res

def test_imgs(img, faces, face_features):
    outputs = []
    for i, face in enumerate(faces):
        output = test_img(img, face, face_features[i])
        outputs.append(output)
    return outputs
