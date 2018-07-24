from urllib.parse import urlparse
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler
import json


class HttpProcessor(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/json; charset=utf-8')
        self.end_headers()

        o = urlparse(self.path)
        req = parse_qs(o.query)

        try:
            if 'data' not in req:
                return

            req = req['data'][0]
            req = json.loads(req)
            response = self.server.handle(req)

            self.write_response(response.get_data())
        except BaseException as e:
            self.wfile.write("{}\n{}".format(e, req).encode())
            raise

    def write_response(self, response: dict):
        self.wfile.write(json.dumps(response).encode())
