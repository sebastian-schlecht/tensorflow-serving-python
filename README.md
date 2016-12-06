# tensorflow-serving-python #
Minimal Python client to communicate with TensorFlow Serving.

### About ###
Python client to communicate with the TensorFlow RPC API. Similar to the examples in the documentation of TensorFlow Serving,
we use gRPC as the RPC client. 

### Known issues ###
- protobuf message definitions are part of this repo (borrowed from TensorFlow Serving [https://github.com/tensorflow/serving]), they could get out of sync as we compile them during installation but don't want TF Serving as a dependency.  
- Due to point 1, ```msg.CopyFrom(other_msg)``` fails due to class checks (the data is similar but the compiled classes differ) when using functionality from tf.contrib. We serialize data first and read it back which is quite slower than a binary copy.

### Installation ###
Check out the source e.g. via ```git clone https://github.com/sebastian-schlecht/tensorflow-serving-python.git``` and run
```python setup.py install```.

### Examples ###
Examples can be found in the examples folder.