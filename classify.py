import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '/opt/caffe/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe
from caffe.proto import caffe_pb2
from PIL import Image

#plt.rcParams['figure.figsize'] = (10, 10)
#plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'simple_deploy.prototxt'
PRETRAINED = 'simple_num_iter_10000.caffemodel'
IMAGE_FILE = sys.argv[1]
MEAN_FILE = '/srv/dataset/num_mean.binaryproto'

mean_blob = caffe_pb2.BlobProto()
mean_data = open( MEAN_FILE , 'rb' ).read()
mean_blob.ParseFromString(mean_data)
mean_arr = np.array( caffe.io.blobproto_to_array(mean_blob) ) 

caffe.set_mode_cpu()
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=mean_arr[0],
                       raw_scale=255)

input_image = caffe.io.load_image(IMAGE_FILE, color=False)
prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
print 'prediction shape:', prediction[0].shape
plt.plot(prediction[0])
print 'predicted class:', prediction[0].argmax()
plt.show()

im = Image.open(IMAGE_FILE)
im.show()
