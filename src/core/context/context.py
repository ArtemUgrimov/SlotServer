
class Context:
    def __init__(self):
        self.attributes = {}

    @property
    def balance(self):
        if 'balance' not in self.attributes:
            self.attributes['balance'] = 0
        return self.attributes['balance']

    @balance.setter
    def balance(self, value):
        self.attributes['balance'] = value