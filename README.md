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

This package depends on the following pip modules, so you might want to install those first:
 - Cython
 - grpcio
 - grpcio-tools
 - tensorflow
 
 
Alternatively, we offer an unofficial python wheel to be installed with:
```pip install http://www.mealomi.com/storage/tensorflow_serving_python/tensorflow_serving_python-0.1-py2-none-any.whl```

*Note*
When running on Linux, make sure pip is upgraded via ```pip install --upgrade pip``` such that TensorFlow is installed correctly.

### Examples ###
Examples can be found in the examples folder.