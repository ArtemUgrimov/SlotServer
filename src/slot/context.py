from src.core.context.context import Context


class SlotContext(Context):

    @property
    def shifts(self):
        if 'shifts' not in self.attributes:
            self.attributes['shifts'] = []
        return self.attributes['shifts']

    @property
    def window(self):
        if 'window' not in self.attributes:
            self.attributes['window'] = []
        return self.attributes['window']

    @window.setter
    def window(self, value):
        self.attributes['window'] = value

    @shifts.setter
    def shifts(self, value):
        self.attributes['shifts'] = value

    @property
    def wins(self):
        if 'wins' not in self.attributes:
            self.attributes['wins'] = []
        return self.attributes['wins']

    @wins.setter
    def wins(self, value):
        self.attributes['wins'] = value

    @property
    def bet(self):
        if 'bet' not in self.attributes:
            self.attributes['bet'] = 0
        return self.attributes['bet']

    @bet.setter
    def bet(self, value):
        self.attributes['bet'] = value

    @property
    def total_win(self):
        total = 0
        for win in self.wins:
            total += win['coeff'] * self.bet
        return total