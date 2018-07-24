import json


class ResponseStatusCodes:
    OK = 200
    ERROR = 500


class Response:
    def __init__(self):
        self.raw_response = {}
        self.status = ResponseStatusCodes.OK

    def fill_response(self, game):
        pass

    def get_data(self):
        self.raw_response['status'] = self.status
        return json.dumps(self.raw_response, indent=4, sort_keys=True)

    def __getitem__(self, key):
        return self.raw_response[key]

    def __setitem__(self, key, value):
        self.raw_response[key] = value