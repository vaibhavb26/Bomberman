class board():
	
	def __init__(self):
		self.matrix=[[' ' for i in range(76)]for j in range(38)]
	
	def getBoard(self):
		return self.matrix
	