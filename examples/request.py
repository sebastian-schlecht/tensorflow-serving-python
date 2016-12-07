import argparse

from tensorflow_serving_python.client import TFClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RPC Test.')

    parser.add_argument('--host', required=True, type=str, help='Hostname to query')
    parser.add_argument('--port', required=True, type=str, help='Port to query')

    args = parser.parse_args()

    data = open("cat.jpg", "rb").read()
    client = TFClient(args.host, args.port)
    print client.make_prediction(data, timeout=5)
