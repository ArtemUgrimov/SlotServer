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