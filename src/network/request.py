
class Request:
    def __init__(self, request: dict):
        self.raw_request = request
        self.command = request['command']
        self.user_id = request['user_id']

    def __getitem__(self, key):
        return self.raw_request[key]
