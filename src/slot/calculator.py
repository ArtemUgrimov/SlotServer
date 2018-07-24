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
                window_reel.append(reel[(game.context.shifts[reel_id] + pos) % len(reel)])
            window.append(window_reel)
        game.context.window = window

    def calc_lines(self, game):
        window = game.context.window
        wins = []
        for payline in game.rule.paylines:

            first_index = (len(window) - 1) if payline.direction != 'lr' else 0
            increment = -1 if payline.direction != 'lr' else 1

            length = 0
            calc_symbol_id = window[first_index][payline.path[0] - 1]
            for reel_id in range(len(payline.path)):
                if calc_symbol_id == window[reel_id][payline.path[reel_id] - 1]:
                    length = length + increment
                else:
                    break
            coeff = self.get_coeff_for_sym_len(game.rule, calc_symbol_id, length)
            if coeff is None:
                continue

            win = {
                'coeff': coeff,
                'symbol': calc_symbol_id,
                'length': length,
                'payline': payline.id
            }
            wins.append(win)
        game.context.wins = wins

    def get_coeff_for_sym_len(self, rule, symbol, length):
        combinations = rule.paytable
        sym_combos = getattr(combinations, str(symbol))
        coeff = getattr(sym_combos, str(length), None)
        return coeff