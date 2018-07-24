from src.core.engine.calculations.calculator import Calculator
import random


class SlotIdleCalculator(Calculator):
    def calculate(self, game):
        self.rotate_reels(game)
        self.define_window(game)
        self.calc_lines(game)

    def rotate_reels(self, game):
        reels = getattr(game.rule.reels, game.engine.state.state_name, game.rule.reels.idle)
        reels_count = len(reels)

        shifts = []
        for i in range(reels_count):
            reel = reels[i]
            shifts.append(random.randint(0, len(reel) - 1))
        game.context.shifts = shifts

    def define_window(self, game):
        reels = getattr(game.rule.reels, game.engine.state.state_name, game.rule.reels.idle)
        reels_count = len(reels)
        window_height = game.rule.height

        window = []
        for reel_id in range(reels_count):
            window_reel = []
            reel = reels[reel_id]
            for pos in range(window_height):
                window_reel.append(reel[game.context.shifts[reel_id]] + pos)
            window.append(window_reel)
        game.context.window = window

    def calc_lines(self, game):
        pass