import os
from tensorflow.python import pywrap_tensorflow

model_dir = "E:/toolbox/presence-master/GazeCapture/models/itracker_tf/model-23"
#checkpoint_path = os.path.join(model_dir,"model-23")
reader = pywrap_tensorflow.NewCheckpointReader(model_dir)

var_to_shape_map = reader.get_variable_to_shape_map()

for key in var_to_shape_map:
    print("tensor_name: ",key,end='\n')
    #print(reader.get_tensor(key))