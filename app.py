import tkinter as tk

import level_info  # level info

EAZY = 1
NORMAL = 2
HARD = 3
		
class App:
	def __init__(self, master):
		self.frame = tk.Frame(master)
		self.frame.pack()
		self.menu()
		self.virtual = tk.PhotoImage(file = "virtual.png")
		self.flag = tk.PhotoImage(file = "mini_flag.png")

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
		self.frame.config(width = 300, height = 300)
		self.clean_view()
		self.game_view(EAZY)

	def normal(self):
		self.frame.config(width = 470, height = 470)
		self.clean_view()
		self.game_view(NORMAL)

	def hard(self):
		self.frame.config(width = 800, height = 500)
		self.clean_view()
		self.game_view(HARD)

	def clean_view(self):
		for widget in self.frame.winfo_children():
			widget.destroy()

	## menu label and bomb flag count
	def game_info_view(self, lel):

		self.info_grid = tk.Frame(self.frame)
		self.info_grid.place(x = 20, y = 20)
		self.return_btn = tk.Button(self.info_grid, text = "menu", width = 10, command = self.menu)
		self.return_btn.pack(side = tk.LEFT)

		bomb = level_info.level_list[lel][0]
		flag = level_info.level_list[lel][1]
		
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

	def game_grid_view(self,lel):
		self.width = level_info.level_list[lel][2]
		self.height = level_info.level_list[lel][3]

		self.grid_frame = tk.Frame(self.frame)
		self.grid_frame.place(x = 50, y = 70)
		self.btn_list = [[0 for x in range(self.width)] for y in range(self.height)]
		self.btn_val = [[0 for x in range(self.width)] for y in range(self.height)]
		self.game_table = level_info.get_game_table(lel)
		
		for x in range(self.height):	
			for y in range(self.width):
				self.btn_val[x][y] = tk.IntVar(value = self.game_table[x][y])
				self.btn_list[x][y] = tk.Button(self.grid_frame, image = self.virtual, width = 15, height = 15)
				self.btn_list[x][y].bind("<Button-1>", lambda evt, x = x, y = y: self.left_click(x, y))
				self.btn_list[x][y].bind("<Button-3>", lambda evt, x = x, y = y: self.right_click(x, y))
				self.btn_list[x][y].grid(column= y, row= x, padx = 1, pady = 1)



	def test_bomb(self):
		for x in range(self.height):	
			for y in range(self.width):
				status = self.btn_val[x][y].get()
				if status :
					self.btn_list[x][y].config(bg = 'black')

	def game_view(self, lel):
		self.game_info_view(lel)
		self.game_grid_view(lel)

	def left_click(self, x, y):
		print("LEFT")
		#self.test_bomb()
	
	def right_click(self, x, y):
		status = self.btn_val[x][y].get()
		flag_count = self.fc.get()

		if status >= 10 :
			self.btn_list[x][y].config(image = self.virtual)
			self.btn_val[x][y].set(status - 10)
			self.fc.set(flag_count + 1)
			return

		if flag_count != 0 and status < 10:
			self.btn_list[x][y].config(image = self.flag)
			self.btn_val[x][y].set(status + 10)
			self.fc.set(flag_count - 1)
			return


if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()
