from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import traceback
import json


class HttpProcessor(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/json; charset=utf-8')
		self.end_headers()

		o = urlparse.urlparse(self.path)
		req = urlparse.parse_qs(o.query)

		try:
			if 'data' not in req:
				return

			req = req['data'][0]
			req = json.loads(req)

			if req['command'] == 'info':
				self.wfile.write('sessions ' + str(self.server.sessions))
				return

			response = self.server.handle(req)

			self.wfile.write(response)
		except BaseException, e:
			self.wfile.write(str(e) + '\n' + str(req))
			raise