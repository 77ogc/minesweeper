# 9×9 10顆
# 16×16 40顆地
# 30×16 99顆地雷

import random

class LevleInfo():
	EAZY = 1
	NORMAL = 2
	HARD = 3

	def new_table(self, level):
		self.__cal_bomb_table(level)
		self.__cal_bomb_arround_for_dispaly_table()

	def get_bomb_table(self):
		return self.__bomb_table

	def get_diplay_table(self):
		return self.__display_table

	def get_level_list(self):
		level_list = []
		level_1 = [10,10,9,9]
		level_2 = [40,40,16,16]
		level_3 = [99,99,30,16]
		level_list.append([])
		level_list.append(level_1)
		level_list.append(level_2)
		level_list.append(level_3)
		return level_list

	def __cal_bomb_arround_for_dispaly_table(self):
		col = len(self.__bomb_table)
		row = len(self.__bomb_table[0])
		self.__display_table = [[0 for x in range(row)] for y in range(col)]
		for x in range(col):	
			for y in range(row):
				if self.__bomb_table[x][y] == 1:
					if x - 1 > 0 and y - 1 > 0 : self.__display_table[x-1][y-1] += 1
					if y - 1 > 0 : self.__display_table[x][y-1] += 1
					if x + 1 < col and y - 1 > 0 : self.__display_table[x+1][y-1] += 1
					if x - 1 > 0 : self.__display_table[x-1][y] += 1
					if x + 1 < col : self.__display_table[x+1][y] += 1
					if x - 1 > 0 and y + 1 < row : self.__display_table[x-1][y+1] += 1
					if y + 1 < row : self.__display_table[x][y+1] += 1
					if x + 1 < col and y + 1 < row : self.__display_table[x+1][y+1] += 1
		return self.__display_table


	def __cal_bomb_table(self,level):
		if level == self.EAZY:
			self.__bomb_table = [[0 for x in range(9)] for y in range(9)]
			num = random.sample(range(81), 10)	
			for i in num:
				x = i / 9
				y = i % 9
				self.__bomb_table[int(x)][y] = 1
		elif level == self.NORMAL:
			self.__bomb_table = [[0 for x in range(16)] for y in range(16)]
			num = random.sample(range(256), 40)	
			for i in num:
				x = i / 16
				y = i % 16
				self.__bomb_table[int(x)][y] = 1
		elif level == self.HARD:
			self.__bomb_table = [[0 for x in range(16)] for y in range(30)]
			num = random.sample(range(480), 99)	
			for i in num:
				x = i % 30
				y = i / 30
				self.__bomb_table[x][int(y)] = 1
		

		return self.__cal_bomb_arround_for_dispaly_table()

	