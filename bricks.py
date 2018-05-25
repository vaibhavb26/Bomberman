from random import *
class bricks():
	
	def __init__(self,matrix):
		self.matrix=matrix
	
	# make_bricks function plots the bricks
	def make_bricks(self):
		for i in range(20):
			rand1,rand2=0,0
			while (rand1==0 or rand2==0):
				rand1=randint(2,35)
				rand2=randint(4,71)
				if(self.matrix[rand1][rand2]!=' '):
					rand1=0
					rand2=0
				else:
					if rand1%4==2:
						x=rand2%4
						y=rand2%4
						z=rand2
						while x>=0:
							self.matrix[rand1][rand2]='/'
							self.matrix[rand1+1][rand2]='/'
							x-=1
							rand2-=1
						while y<=3:
							self.matrix[rand1][z]='/'
							self.matrix[rand1+1][z]='/'
							y+=1
							z+=1

					elif rand1%4==3:
						x=rand2%4
						y=rand2%4
						z=rand2
						while x>=0:
							self.matrix[rand1][rand2]='/'
							self.matrix[rand1-1][rand2]='/'
							x-=1
							rand2-=1
						while y<=3:
							self.matrix[rand1][z]='/'
							self.matrix[rand1-1][z]='/'
							y+=1
							z+=1


					elif rand1%4==0:
						x=rand2%4
						y=rand2%4
						z=rand2
						while x>=0:
							self.matrix[rand1][rand2]='/'
							self.matrix[rand1+1][rand2]='/'
							x-=1
							rand2-=1
						while y<=3:
							self.matrix[rand1][z]='/'
							self.matrix[rand1+1][z]='/'
							y+=1
							z+=1

					else:
						x=rand2%4
						y=rand2%4
						z=rand2
						while x>=0:
							self.matrix[rand1][rand2]='/'
							self.matrix[rand1-1][rand2]='/'
							x-=1
							rand2-=1
						while y<=3:
							self.matrix[rand1][z]='/'
							self.matrix[rand1-1][z]='/'
							y+=1
							z+=1
		return self.matrix