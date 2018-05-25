class bomb():
	
	def __init__(self):
		self.flag=0
		self.a=[0,]

	#plant the bomb	
	def plant(self,matrix,x,y):
		for i in range (0,2):
			for j in range (0,4):
				matrix[x+i][y+j] = 'O'
		return matrix

	#explosion after 3 frames
	def blast(self,matrix,x,y,player_x,player_y,score):
		for i in range (0,2):
			for j in range (0,4):
				matrix[x+i][y+j] = 'e'
		
		if matrix[x][y] == '\u001b[0;31mE\u001b[0m' :
			score += 100
		
		if(x == player_x and y == player_y):
			self.flag = 1
		
		if(matrix[x-1][y] != 'X'):
			if(matrix[x-2][y] == '\u001b[0;36mB\u001b[0m'):
				self.flag=1
			if(matrix[x-2][y] == '\u001b[0;31mE\u001b[0m'):
				self.a.append(x-2)
				self.a.append(y)
				score += 100
			if(matrix[x-2][y] == '/'):
				score += 20
			for i in range (0,2):
				for j in range (0,4):
					matrix[x-2+i][y+j] = 'e'
		if(matrix[x+2][y] != 'X'):
			if(matrix[x+2][y] == '\u001b[0;36mB\u001b[0m'):
				self.flag = 1
			if(matrix[x+2][y] == '\u001b[0;31mE\u001b[0m'):
				self.a.append(x+2)
				self.a.append(y)
				score += 100
			if(matrix[x+2][y] == '/'):
				score += 20
			for i in range (0,2):
				for j in range (0,4):
					matrix[x+2+i][y+j] = 'e'

		if(matrix[x][y+4] != 'X'):
			if(matrix[x][y+4] == '\u001b[0;36mB\u001b[0m'):
				self.flag=1
			if(matrix[x][y+4] == '\u001b[0;31mE\u001b[0m'):
				self.a.append(x)
				self.a.append(y+4)
				score += 100
			if(matrix[x][y+4] == '/'):
				score += 20
			for i in range (0,2):
				for j in range (0,4):
					matrix[x+i][y+4+j] = 'e'

		if(matrix[x][y-4] != 'X'):
			if(matrix[x][y-4] == '\u001b[0;36mB\u001b[0m'):
				self.flag=1
			if(matrix[x][y-4] == '\u001b[0;31mE\u001b[0m'):
				self.a.append(x)
				self.a.append(y-4)
				score += 100
			if(matrix[x][y-4] == '/'):
				score += 20
			for i in range (0,2):
				for j in range (1,5):
					matrix[x+i][y-j] = 'e'

		return matrix,self.a,score

	#restore the original matrix after 1 frame of explosion
	def restore(self,matrix,x,y):
		for i in range (0,2):
			for j in range (0,4):
				matrix[x+i][y+j] = ' '

		if(matrix[x-1][y] != 'X'):
			for i in range (1,3):
				for j in range (0,4):
					matrix[x-i][y+j] = ' '

		if(matrix[x+2][y] != 'X'):
			for i in range (0,2):
				for j in range (0,4):
					matrix[x+2+i][y+j] = ' '

		if(matrix[x][y+4] != 'X'):
			for i in range (0,2):
				for j in range (0,4):
					matrix[x+i][y+4+j] = ' '

		if(matrix[x][y-1]!='X'):
			for i in range (0,2):
				for j in range (1,5):
					matrix[x+i][y-j] = ' '
		return matrix,self.flag
