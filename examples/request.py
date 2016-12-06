import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from tensorflow_serving_python.client import TFClient

if __name__ == "__main__":
    data = open("cat.jpg", "rb").read()
    client = TFClient("localhost", "9000")
    print client.make_prediction(data)
