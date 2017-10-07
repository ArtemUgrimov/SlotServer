from http_processor import HttpProcessor
from server import Server


serv = Server(("localhost", 80), HttpProcessor)
serv.serve_forever()