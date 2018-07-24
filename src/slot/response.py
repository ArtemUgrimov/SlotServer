from src.network.response import Response


class SlotResponse(Response):
    def fill_response(self, game):
        super().fill_response(game)
        context = game.context

        self.raw_response['balance'] = context.balance
        self.raw_response['window'] = context.window
