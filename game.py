from board import *
from wall import *
from bricks import *
from player import *
from bomb import *
from enemy import *
import sys, tty, termios,os

 
os.system("clear") 
matrix=board()
matrix=matrix.getBoard()
matrix=wall(matrix)
matrix=matrix.make_wall()
matrix=bricks(matrix)
matrix=matrix.make_bricks()
player_obj=player()
matrix=player_obj.display_pos(matrix)
enemy_obj=enemy()
move_obj=enemy_obj.make_enemy(matrix)
bomb_obj=bomb()
lives=3
score=0
for i in range(38):
	for j in range(76):
		print(move_obj[i][j],end='')
	print('')
print("LIVES="+str(lives))
print("SCORE="+str(score))
bomb_plant = False
bomb_x = 0
bomb_y = 0
count = 0
bomb_blast = False
count2 = 0
flag = 0
enemy_flag = 0
game_over = 0
a=[0,]
while(True):	
	x=player_obj.get_pos_x(move_obj)
	y=player_obj.get_pos_y(move_obj)

	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	if ch=='q':
		break
	elif ch=='w':
		matrix=player_obj.up(move_obj,x,y)
	elif ch=='s':
		matrix=player_obj.down(move_obj,x,y)
	elif ch=='a':
		matrix=player_obj.left(move_obj,x,y)
	elif ch=='d':
		matrix=player_obj.right(move_obj,x,y)
	elif ch=='b':
		if(bomb_plant == False):
			bomb_x=x
			bomb_y=y
			matrix=bomb_obj.plant(move_obj,x,y)
			bomb_plant=True
			count=0
	if (bomb_plant == True):
		for i in range(0,2):
			for j in range(0,4):
				matrix[bomb_x+i][bomb_y+j] = 'O'
		count += 1
	matrix,enemy_flag=enemy_obj.move_enemy(move_obj,a)
	if(count == 4):
		matrix,a,score=bomb_obj.blast(move_obj,bomb_x,bomb_y,x,y,score)
		bomb_blast=True
		count=0
	if(bomb_blast == True):
		count2+=1
	os.system("clear")

	if(count2 == 2):
		matrix,flag=bomb_obj.restore(matrix,bomb_x,bomb_y)
		count2=0
		bomb_blast=False
		bomb_plant=False	

	if(flag == 1 or enemy_flag == 1 or player_obj.flag == 1):
		lives-=1
		for i in range (2,4):
			for j in range (4,8):
				matrix[i][j]='\u001b[0;36mB\u001b[0m'
		for i in range (4,6):
			for j in range (4,8):
				matrix[i][j]=' '
		for i in range (2,4):
			for j in range (8,12):
				matrix[i][j]=' '
		bomb_obj.flag = 0	
		flag = 0
		enemy_flag = 0
		enemy_obj.flag = 0
		bomb_plant = False
		count = 0
		count2 = 0
		player_obj.flag = 0
		for i in range(2,37):
			for j in range(4,73):
				if matrix[i][j] == 'O':
					matrix[i][j] = ' '
		print("LIFE LOST :(")
		if lives == 0:
			game_over = 1
	for i in range(38):
		for j in range(76):
			print(matrix[i][j],end='')
		print('')
	print("LIVES=" + str(lives))
	print("SCORE=" + str(score))
	if game_over == 1:
		print("GAME OVER")
		break
	if (enemy_obj.flag1 == 1 and enemy_obj.flag2 == 1 and enemy_obj.flag3 == 1):
		print("YOU WON!")
		break