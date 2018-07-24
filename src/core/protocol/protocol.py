from src.network.response import Response, ResponseStatusCodes


class Protocol:
    def __init__(self, game):
        self.game = game
        self.context = game.context
        self.request = None
        self.responses = {}

    def get_response_obj(self, state: str, action: str):
        try:
            return self.responses['{}_{}'.format(state, action)]
        except:
            raise BaseException('There is no response for state "{}" and action "{}"'.format(state, action))

    def add_response_obj(self, state: str, action: str, response: Response):
        self.responses['{}_{}'.format(state, action)] = response

    def prepare(self):
        state = self.game.engine.prior_state.state_name
        action = self.request.command
        response = self.get_response_obj(state, action)

        response['command'] = self.request.command
        response['status'] = ResponseStatusCodes.OK

    def get_response(self):
        self.prepare()

        state = self.game.engine.prior_state.state_name
        action = self.request.command
        response = self.get_response_obj(state, action)

        response.fill_response(self.game)
        self.update_response(response)

        self.finalize()
        return response

    def update_response(self, response):
        # response['test'] = 'da'
        pass

    def finalize(self):
        pass