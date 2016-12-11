# tensorflow-serving-python #
Minimal Python client to communicate with TensorFlow Serving.

### About ###
Python client to communicate with the TensorFlow RPC API. Similar to the examples in the documentation of TensorFlow Serving,
we use gRPC as the RPC client.

### TODOs ###
- Link TensorFlow Serving as a sub-module here. To compile protobufs properly during build.  
- When distributing, get rid of tf.contrib functions to remove TensorFlow as a dependency.

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
