# 9×9 10顆
# 16×16 40顆地
# 30×16 99顆地雷

import random

EAZY = 1
NORMAL = 2
HARD = 3

level_list = []
level_1 = [10,10,9,9]
level_2 = [40,40,16,16]
level_3 = [99,99,30,16]
level_list.append([])
level_list.append(level_1)
level_list.append(level_2)
level_list.append(level_3)



def add_bomb_arround(table):
	return table

def get_game_table(level):
	if level == EAZY:
		game_table = [[0 for x in range(9)] for y in range(9)]
		num = random.sample(range(81), 10)	
		for i in num:
			x = i / 9
			y = i % 9
			game_table[int(x)][y] = 1
	elif level == NORMAL:
		game_table = [[0 for x in range(16)] for y in range(16)]
		num = random.sample(range(256), 40)	
		for i in num:
			x = i / 16
			y = i % 16
			game_table[int(x)][y] = 1
	elif level == HARD:
		game_table = [[0 for x in range(30)] for y in range(16)]
		num = random.sample(range(480), 99)	
		for i in num:
			x = i / 30
			y = i % 30
			game_table[int(x)][y] = 1
	
	return add_bomb_arround(game_table)