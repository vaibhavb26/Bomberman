class player():
	
	def __init__(self):
		self.x = 2
		self.y = 4
		self.flag = 0
	#initial position is displayed
	def display_pos(self,matrix):
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.x+i][self.y+j] = '\u001b[0;36mB\u001b[0m'
		return matrix
	# returns the x co ordinate of position of bomberman
	def get_pos_x(self,matrix):
		flag1,flag2 = 0,0
		for i in range(38):
			for j in range(76):
				if(matrix[i][j] == '\u001b[0;36mB\u001b[0m'):
					self.x = i
					flag1 = 1
					break
				elif(matrix[i][j] == 'O'):
					if(flag2 == 0):
						self.x = i
						flag2 = 1
			if(flag1 == 1):
				break
		return self.x
	
	# returns the y co ordinate of position of bomberman
	def get_pos_y(self,matrix):
		flag3,flag4 = 0,0
		for i in range(38):
			for j in range(76):
				if(matrix[i][j] == '\u001b[0;36mB\u001b[0m'):
					self.y = j
					flag3 = 1
					break
				elif(matrix[i][j] == 'O'):
					if(flag4 == 0):
						self.y = j
						flag4 = 1
			if(flag3 == 1):
				break
		return self.y
	#move right
	def right(self,matrix,x,y):
		if (matrix[x][y+4] != ' ' and matrix[x][y+4] != '\u001b[0;31mE\u001b[0m'):
			return matrix
		elif matrix[x][y+4] == '\u001b[0;31mE\u001b[0m':
			self.flag = 1
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '

			return matrix
		else:
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			for i in range (0,2):
				for j in range (4,8):
					matrix[x+i][y+j] = '\u001b[0;36mB\u001b[0m'
			return matrix

	#move left
	def left(self,matrix,x,y):
		if (matrix[x][y-1] != ' ' and matrix[x][y-1] != '\u001b[0;31mE\u001b[0m'):
			return matrix
		elif matrix[x][y-1] == '\u001b[0;31mE\u001b[0m':
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			self.flag = 1
			return matrix
		else:
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			for i in range (0,2):
				for j in range (1,5):
					matrix[x+i][y-j] = '\u001b[0;36mB\u001b[0m'
			return matrix
	
	#move up
	def up(self,matrix,x,y):
		if (matrix[x-1][y] != ' ' and matrix[x-1][y] != '\u001b[0;31mE\u001b[0m'):
			return matrix
		elif matrix[x-1][y] == '\u001b[0;31mE\u001b[0m':
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			self.flag = 1
			return matrix
		else:
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			for i in range (1,3):
				for j in range (0,4):
					matrix[x-i][y+j] = '\u001b[0;36mB\u001b[0m'
			return matrix
	
	#move down
	def down(self,matrix,x,y):
		if (matrix[x+2][y] != ' ' and matrix[x+2][y] != '\u001b[0;31mE\u001b[0m'):
			return matrix
		elif matrix[x+2][y] == '\u001b[0;31mE\u001b[0m':
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			self.flag = 1
			return matrix
		else:
			for i in range(0,2):
				for j in range(0,4):
					matrix[x+i][y+j] = ' '
			for i in range (0,2):
				for j in range (0,4):
					matrix[x+i+2][y+j] = '\u001b[0;36mB\u001b[0m'
			return matrix