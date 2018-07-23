from src.network.http_processor import HttpProcessor
from src.network.server import Server


def run():
    server = Server(("localhost", 80), HttpProcessor)
    server.serve_forever()


if __name__ == '__main__':
    run()
