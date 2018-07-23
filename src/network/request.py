
class Request:
    def __init__(self, request: dict):
        self.raw_request = request
        self.command = request['command']
        self.user_id = request['userid']

    def __getitem__(self, key):
        return self.raw_request[key]
