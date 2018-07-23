from src.network.request import Request
from src.network.response import Response


class Protocol:
    def __init__(self, context, request: Request):
        self.context = context
        self.request = request
        self.responses = {}

    def get_response_obj(self, state: str, action: str):
        return self.responses['{}_{}'.format(state, action)]

    def add_response_obj(self, state: str, action: str, response: Response):
        self.responses['{}_{}'.format(state, action)] = response

    def prepare(self):
        state = self.context.state
        action = self.context.action
        response = self.get_response_obj(state, action)

        response['command'] = self.request.command
        response['status'] = 'ok'

    def get_response(self):
        state = self.context.state
        action = self.context.action
        response = self.get_response_obj(state, action)

        return response.get_data()

    def finalize(self):
        pass