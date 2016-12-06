import tensorflow as tf
import time
from grpc.beta import implementations
from tensorflow_serving_python.protos import prediction_service_pb2, predict_pb2, tensor_pb2


class TFClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.channel = implementations.insecure_channel(self.host, int(self.port))
        self.stub = prediction_service_pb2.beta_create_PredictionService_stub(self.channel)

    def execute(self, request, timeout=10.0):
        return self.stub.Predict(request, timeout)

    def make_prediction(self, data, name='inception', timeout=10.):
        request = predict_pb2.PredictRequest()
        request.model_spec.name = name
        proto = tf.contrib.util.make_tensor_proto(data, shape=[1])
        s = time.time()
        request.inputs['images'].ParseFromString(proto.SerializeToString())
        e = time.time()
        print e-s
        return self.execute(request, timeout=timeout)
