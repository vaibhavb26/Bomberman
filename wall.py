class wall():
	def __init__(self,matrix):
		self.matrix=matrix

	def make_wall(self):
		for i in range(38):
			for j in range(76):
				if(i == 0 or i == 1 or i == 36 or i == 37 or j == 0 or j == 1 or j == 2 or j == 3 or j == 72 or j == 73 or j == 74 or j == 75):
					self.matrix[i][j]='X'
				elif ((i%4 == 0 or i%4 == 1) and (j%8 == 0 or j%8 == 1 or j%8 == 2 or j%8 == 3)):
					self.matrix[i][j]='X'
		return self.matrix
	#adds walls to the game 
