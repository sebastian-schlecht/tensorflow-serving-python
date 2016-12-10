import argparse
import pprint

from tensorflow_serving_python.client import TFClient

pp = pprint.PrettyPrinter(indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RPC Test.')

    parser.add_argument('--host', required=True, type=str, help='Hostname to query')
    parser.add_argument('--port', required=True, type=str, help='Port to query')
    parser.add_argument('--image', required=True, type=str, help='Image to send (JPG format)')
    args = parser.parse_args()

    data = open(args.image, "rb").read()
    client = TFClient(args.host, args.port)
    pp.pprint(client.make_prediction(data, timeout=10))
