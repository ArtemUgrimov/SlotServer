class Paytable:
	def __init__(self):
		
		self.pt = {
			1 : {3 : 100, 4: 200, 5: 500},
			2 : {3 : 100, 4: 200, 5: 500},
			3 : {3 : 100, 4: 200, 5: 500},
			4 : {3 : 100, 4: 200, 5: 500},
			5 : {3 : 100, 4: 200, 5: 500},
			6 : {3 : 100, 4: 200, 5: 500},
			7 : {3 : 100, 4: 200, 5: 500},
			8 : {3 : 100, 4: 200, 5: 500},
			9 : {3 : 100, 4: 200, 5: 500},
			10 : {3 : 100, 4: 200, 5: 500}
		}

	def get(self, symbol, count):
		if symbol in self.pt and count in self.pt[symbol]:
			return self.pt[symbol][count]
		return 0