PAYLINES_COUNT = 20

class Paylines:
	def __init__(self):
		self.__paylines = []
		
		self.__paylines.append([0, 0, 0, 0, 0])
		self.__paylines.append([1, 1, 1, 1, 1])
		self.__paylines.append([2, 2, 2, 2, 2])
		
		self.__paylines.append([0, 1, 2, 1, 0])
		self.__paylines.append([2, 1, 0, 1, 2])
		
		self.__paylines.append([0, 0, 1, 0, 0])
		self.__paylines.append([2, 2, 1, 2, 2])
		
		self.__paylines.append([0, 0, 1, 2, 2])
		self.__paylines.append([2, 2, 1, 0, 0])
		
		self.__paylines.append([0, 2, 0, 2, 0])
		self.__paylines.append([2, 0, 2, 0, 2])

		self.__paylines.append([1, 2, 2, 1, 0])
		self.__paylines.append([1, 0, 0, 1, 2])
		self.__paylines.append([0, 1, 2, 2, 1])
		self.__paylines.append([2, 1, 0, 0, 1])

	def get_array(self):
		return self.__paylines

	def get_wins(self, window, pt, bet_value):
		print('\n')
		print('Calculating...')
		wins = []
		for pl_index in range(len(self.__paylines)):
			pl = self.__paylines[pl_index]
			print('\tPL : ' + str(pl))
			start = -1
			count_in_line = 1
			for i in range(0, len(pl)):
				if i == 0:
					start = window[i][pl[i]]
					print('\tSYM : ' + str(start))
				else:
					if window[i][pl[i]] == start:
						count_in_line += 1
					else:
						break
			print('\tCOUNT IN LINE : ' + str(count_in_line))
			print('\n')
			win_sum = pt.get(start, count_in_line) * bet_value
			if win_sum != 0:
				win = {}
				win['symbol'] = start
				win['count'] = count_in_line
				win['win'] = win_sum
				win['line'] = pl
				win['line_id'] = pl_index
				wins.append(win)
		
		print('Done')
		print('\n')

		return wins