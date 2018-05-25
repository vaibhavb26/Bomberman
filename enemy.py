from random import *

class enemy():
	
	def __init__(self):
		self.array=[0]
		self.array1=[0,0,0,0]
		self.array2=[0,0,0,0]
		self.array3=[0,0,0,0]
		self.flag=0
		self.flag1=0
		self.flag2=0
		self.flag3=0
		self.enemy1=0
		self.enemy2=0
		self.enemy3=0
	
	#spawn enemies
	def make_enemy(self,matrix):
		for i in range(3):
			rand1=0
			rand2=0
			while(rand1==0 or rand2==0):
				rand1=randint(2,34)
				rand2=randint(4,71)
				if(matrix[rand1][rand2]!=' '):
					rand1=0
					rand2=0
				else:
					while rand2%4!=0:
						rand2-=1
					while (rand1%4!=2 and rand1%4!=0):
						rand1-=1
			for i in range(0,2):
				for j in range(0,4):
					matrix[rand1+i][rand2+j]='\u001b[0;31mE\u001b[0m'
			self.array.append(rand1)
			self.array.append(rand2)
		return matrix	
	#calculates the possible direction for each of the enemy to move
	def move_enemy(self,matrix,a):
		if(len(a)!=1):
			print("len "+str(len(a)))
			print(a)
			for i in range(1,len(a),2):
				if (a[i]==self.array[1] and a[i+1]==self.array[2]):
					self.flag1=1
				if (a[i]==self.array[3] and a[i+1]==self.array[4]):
					self.flag2=1
				if (a[i]==self.array[5] and a[i+1]==self.array[6]):
					self.flag3=1
		rand1,rand2,rand3 = 0,0,0
		self.array1 = [0,0,0,0]
		self.array2 = [0,0,0,0]
		self.array3 = [0,0,0,0]
		if(matrix[self.array[1]-2][self.array[2]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[1]-2][self.array[2]] == ' '):
			self.array1[0] = 1
		if(matrix[self.array[1]+2][self.array[2]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[1]+2][self.array[2]] == ' '):
			self.array1[1] = 1
		if(matrix[self.array[1]][self.array[2]-1] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[1]][self.array[2]-1] == ' '):
			self.array1[2] = 1
		if(matrix[self.array[1]][self.array[2]+4] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[1]][self.array[2]+4] == ' '):
			self.array1[3] = 1
		if(matrix[self.array[3]-2][self.array[4]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[3]-2][self.array[4]] == ' '):
			self.array2[0] = 1
		if(matrix[self.array[3]+2][self.array[4]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[3]+2][self.array[4]] == ' '):
			self.array2[1] = 1
		if(matrix[self.array[3]][self.array[4]-1] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[3]][self.array[4]-1] == ' '):
			self.array2[2] = 1 
		if(matrix[self.array[3]][self.array[4]+4] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[3]][self.array[4]+4] == ' '):
			self.array2[3] = 1
		if(matrix[self.array[5]-2][self.array[6]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[5]-2][self.array[6]] == ' '):
			self.array3[0] = 1
		if(matrix[self.array[5]+2][self.array[6]] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[5]+2][self.array[6]] == ' '):
			self.array3[1] = 1
		if(matrix[self.array[5]][self.array[6]-1] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[5]][self.array[6]-1] == ' '):
			self.array3[2] = 1
		if(matrix[self.array[5]][self.array[6]+4] == '\u001b[0;36mB\u001b[0m' or matrix[self.array[5]][self.array[6]+4] == ' '):
			self.array3[3] = 1

		rand1 = randint(0,3)
		rand2 = randint(0,3)
		rand3 = randint(0,3)
		if (self.flag1 == 1 and self.enemy1 == 0):
			if(matrix[self.array[1]][self.array[2]] == '\u001b[0;31mE\u001b[0m'):
				for i in range(0,2):
					for j in range(0,4):
						matrix[self.array[1]+i][self.array[2]+j] = ' ' 
				self.enemy1 = 1
			self.no_move(1,matrix)
		elif(self.array1[rand1] == 1):
			if rand1 == 0:
				self.move_up(1,matrix)
			elif rand1 == 1:
				self.move_down(1,matrix)
			elif rand1 == 2:
				self.move_left(1,matrix)
			elif rand1 == 3:
				self.move_right(1,matrix)
		elif(self.array1 == [0,0,0,0]):
			self.no_move(1,matrix)
		else:
			while(self.array1[rand1] != 1 ):
				rand1 = randint(0,3)
			if rand1 == 0:
				self.move_up(1,matrix)
			elif rand1 == 1:
				self.move_down(1,matrix)
			elif rand1 == 2:
				self.move_left(1,matrix)
			elif rand1 == 3:
				self.move_right(1,matrix)
		if (self.flag2 == 1 and self.enemy2 == 0):
			if(matrix[self.array[3]][self.array[4]]=='\u001b[0;31mE\u001b[0m'):
				for i in range(0,2):
					for j in range(0,4):
						matrix[self.array[3]+i][self.array[4]+j] = ' '
				self.enemy2 = 1
			self.no_move(2,matrix)
		elif(self.array2[rand2] == 1):
			if rand2 == 0:
				self.move_up(2,matrix)
			elif rand2 == 1:
				self.move_down(2,matrix)
			elif rand2 == 2:
				self.move_left(2,matrix)
			elif rand2 == 3:
				self.move_right(2,matrix)
		elif(self.array2 == [0,0,0,0]):
			self.no_move(2,matrix)
		else:
			while(self.array2[rand2] != 1 ):
				rand2 = randint(0,3)
			if rand2 == 0:
				self.move_up(2,matrix)
			elif rand2 == 1:
				self.move_down(2,matrix)
			elif rand2 == 2:
				self.move_left(2,matrix)
			elif rand2 == 3:
				self.move_right(2,matrix)
		if (self.flag3 == 1 and self.enemy3 == 0):
			if(matrix[self.array[5]][self.array[6]] == '\u001b[0;31mE\u001b[0m'):
				for i in range(0,2):
					for j in range(0,4):
						matrix[self.array[5]+i][self.array[6]+j] = ' '
				self.enemy3=1
			self.no_move(3,matrix)
		elif(self.array3[rand3] == 1):
			if rand3 == 0:
				self.move_up(3,matrix)
			elif rand3 == 1:
				self.move_down(3,matrix)
			elif rand3 == 2:
				self.move_left(3,matrix)
			elif rand3 == 3:
				self.move_right(3,matrix)
		elif(self.array3 == [0,0,0,0]):
			self.no_move(3,matrix)
		else:
			while(self.array3[rand3] != 1 ):
				rand3 = randint(0,3)
			if rand3 == 0:
				self.move_up(3,matrix)
			elif rand3 == 1:
				self.move_down(3,matrix)
			elif rand3 == 2:
				self.move_left(3,matrix)
			elif rand3 == 3:
				self.move_right(3,matrix)
		return matrix,self.flag

	#move up	
	def move_up(self,num,matrix):
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]+j] = ' '

		if(matrix[self.array[num*2-1]-1][self.array[num*2]]=='\u001b[0;36mB\u001b[0m'):
			self.flag=1
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]-i-1][self.array[num*2]+j] = '\u001b[0;31mE\u001b[0m'
		self.array[num*2-1]=self.array[num*2-1]-2
		return matrix

	#move down
	def move_down(self,num,matrix):
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]+j] = ' '

		if(matrix[self.array[num*2-1]+2][self.array[num*2]]=='\u001b[0;36mB\u001b[0m'):
			self.flag=1
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i+2][self.array[num*2]+j] = '\u001b[0;31mE\u001b[0m'
		self.array[num*2-1]=self.array[num*2-1]+2
		return matrix

	#move left
	def move_left(self,num,matrix):
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]+j] = ' '

		if(matrix[self.array[num*2-1]][self.array[num*2]-4]=='\u001b[0;36mB\u001b[0m'):
			self.flag=1
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]-j-1] = '\u001b[0;31mE\u001b[0m'
		self.array[num*2]=self.array[num*2]-4
		return matrix

	#move right
	def move_right(self,num,matrix):
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]+j] = ' '
		if(matrix[self.array[num*2-1]][self.array[num*2]+4]=='\u001b[0;36mB\u001b[0m'):
			self.flag=1
		for i in range(0,2):
			for j in range(0,4):
				matrix[self.array[num*2-1]+i][self.array[num*2]+j+4] = '\u001b[0;31mE\u001b[0m'
		self.array[num*2]=self.array[num*2]+4
		return matrix

	#don't move	
	def no_move(self,num,matrix):
		return matrix
