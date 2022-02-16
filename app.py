import tkinter as tk

import level_info  # level info
		
class App:
	def __init__(self, master):
		self.frame = tk.Frame(master)
		self.frame.pack()
		self.menu()
		self.virtual = tk.PhotoImage(file = "virtual.png")
		self.flag = tk.PhotoImage(file = "mini_flag.png")
		self.game_info = level_info.LevleInfo()

	def menu(self):
		self.clean_view()
		self.frame.config(width = 120, height = 150)
		self.eazy_btn = tk.Button(self.frame, text = "EAZY", width = 10, command = self.eazy)
		self.noraml_btn = tk.Button(self.frame, text = "NORMAL", width = 10, command = self.normal)
		self.hard_btn = tk.Button(self.frame, text = "HARD", width = 10, command = self.hard)
		self.eazy_btn.grid(column = 0, row = 0, padx = 20, pady = 10)
		self.noraml_btn.grid(column = 0, row = 1, pady = 10)
		self.hard_btn.grid(column = 0, row = 2, pady = 10)

	def eazy(self):
		level = self.game_info.EAZY
		self.frame.config(width = 300, height = 300)
		self.clean_view()
		self.game_view(level)

	def normal(self):
		level = self.game_info.NORMAL
		self.frame.config(width = 465, height = 475)
		self.clean_view()
		self.game_view(level)

	def hard(self):
		level = self.game_info.HARD
		self.frame.config(width = 800, height = 500)
		self.clean_view()
		self.game_view(level)

	def game_view(self, level):
		self.game_info_view(level)
		self.game_grid_view(level)

	def clean_view(self):
		for widget in self.frame.winfo_children():
			widget.destroy()

	## menu label and bomb flag count
	def game_info_view(self, level):

		self.info_grid = tk.Frame(self.frame)
		self.info_grid.place(x = 20, y = 20)
		self.return_btn = tk.Button(self.info_grid, text = "menu", width = 10, command = self.menu)
		self.return_btn.pack(side = tk.LEFT)

		game_list = self.game_info.get_level_list()

		bomb = game_list[level][0]
		flag = game_list[level][1]
		
		self.bc = tk.IntVar(value = bomb)
		self.fc = tk.IntVar(value = flag)

		self.bomb_info = tk.Label(self.info_grid, width = 3, textvariable = self.bc)
		self.flag_info = tk.Label(self.info_grid, width = 3, textvariable = self.fc)
		self.bomb_label = tk.Label(self.info_grid,text = 'Bomb :', width = 5)
		self.flag_label = tk.Label(self.info_grid,text = 'Flag :', width = 5)

		
		self.bomb_label.pack(side = tk.LEFT, padx = 10)
		self.bomb_info.pack(side = tk.LEFT)
		self.flag_label.pack(side = tk.LEFT, padx = 10)
		self.flag_info.pack(side = tk.LEFT)

	def game_grid_view(self,level):

		game_list = self.game_info.get_level_list()

		self.width = game_list[level][2]
		self.height = game_list[level][3]

		self.grid_frame = tk.Frame(self.frame)
		self.grid_frame.place(x = 50, y = 70)
		self.btn_list = [[0 for x in range(self.height)] for y in range(self.width)]
		self.btn_val = [[0 for x in range(self.height)] for y in range(self.width)]
		self.btn_is_flaged = [[0 for x in range(self.height)] for y in range(self.width)]
		
		self.game_info.new_table(level)

		display_table = self.game_info.get_diplay_table()
		bomb_table =  self.game_info.get_bomb_table()
		
		for x in range(self.width):	
			for y in range(self.height):
				self.btn_val[x][y] = tk.IntVar(value = display_table[x][y])
				self.btn_list[x][y] = tk.Button(self.grid_frame, image = self.virtual, width = 15, height = 15)
				self.btn_list[x][y].bind("<Button-1>", lambda evt, x = x, y = y: self.left_click_for_flag(x, y))
				self.btn_list[x][y].bind("<Button-3>", lambda evt, x = x, y = y: self.right_click_for_reveal(x, y))
				self.btn_list[x][y].grid(column= x, row= y, padx = 1, pady = 1)
				#self.btn_list[x][y].config(text = str(self.btn_val[x][y].get()), compound = 'c')
				



	def test_bomb(self):
		for x in range(self.height):	
			for y in range(self.width):
				status = self.btn_val[x][y].get()
				if status :
					self.btn_list[x][y].config(bg = 'black')


	def left_click_for_flag(self, x, y):
		#self.test_bomb()
		if self.btn_is_flaged[x][y] : return

		

	
	def right_click_for_reveal(self, x, y):

		isFlaged = self.btn_is_flaged[x][y]
		flag_count = self.fc.get()

		if isFlaged :
			self.btn_list[x][y].config(image = self.virtual)
			self.btn_is_flaged[x][y] = 0
			self.fc.set(flag_count + 1)
			return

		if flag_count != 0 :
			self.btn_list[x][y].config(image = self.flag)
			self.btn_is_flaged[x][y] = 1
			self.fc.set(flag_count - 1)
			return




if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()
