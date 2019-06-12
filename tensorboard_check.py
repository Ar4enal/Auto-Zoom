import tensorflow as tf
import os

model_dir = os.path.dirname(os.path.realpath(__file__)) + "/GazeCapture/models/itracker_tf"

sess = tf.Session()

saver = tf.train.import_meta_graph(model_dir+'/model-23.meta')
saver.restore(sess,tf.train.latest_checkpoint(model_dir))

summary_writer = tf.summary.FileWriter('E:/toolbox', tf.get_default_graph())


