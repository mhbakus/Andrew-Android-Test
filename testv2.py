import random
import time
import os
#class cell for represent a cell
class Cell:
	def __init__(self, status):
		self.is_alive = status
		self.statut = '0' if status else ' '

	def __repr__(self):
		return '{}'.format(self.statut)

	def get_cell(self):
		return self.statut

	def update_status(self, status):
		self.is_alive = status
		self.statut = '0' if status else ' '


#class celltable for represent a table of cells
class CellTable:
	def __init__(self, cellist = []):
		self.cells = cellist
		self.create_cell_list()

	def create_cell_list(self):
		choix = (True, False)
		for _ in range(10):
			self.dumy_list = []
			for _ in range(10):
				self.dumy_list.append(Cell(random.choice(choix)))
			self.add_cell(self.dumy_list)

	def add_cell(self, cell = []):
		self.cells.append(cell)

	def get_cells(self):

		for cell in self.cells:
			mystr = ''
			for celobj in cell:
				mystr += ' ' + celobj.get_cell()
			print(mystr)

	def __is_valid(self, y, x):
		if y in range(10) and x in range(10): #y = -5, x = -55 ??
			return True
		else:
			return False

	def get_cel(self, y, x):
		return self.cells[y][x]

	def get_up_left(self, y, x):
		#TODO: Check for out of range on x, as well as y
		if self.__is_valid(y,x):
			if y == 0 and x in range(10):
				return 'none'
			else:
				return self.cells[y-1][x-1]
		else:
			raise ValueError("this is not a valid cell check the range")

	def get_up_right(self, y, x):
		if self.__is_valid(y,x):
			if y == 0 or x == 9:
				return 'none'
			else:
				return self.cells[y-1][x+1]
		else:
			raise ValueError("this is not a valid cell check the range")

	def get_down_left(self, y, x):
		if self.__is_valid(y,x):
			if y == 9 and x in range(10):
				return 'none'
			else:
				return self.cells[y+1][x-1]
		else:
			raise ValueError("this is not a valid cell check the range")


	def get_down_right(self, y, x):
		if self.__is_valid(y,x):
			if y == 9 or x == 9:
					return 'none'
			else:
				return self.cells[y+1][x+1]
		else:
			raise ValueError("this is not a valid cell check the range")

	def get_left(self, y, x):
		if self.__is_valid(y,x):
			if y in range(10) and x == 0:
					return 'none'
			else:
				return self.cells[y][x-1]
		else:
			raise ValueError("this is not a valid cell check the range")

	def get_right(self, y, x):
		if self.__is_valid(y,x):
			if y in range(10) and x == 9:
					return 'none'
			else:
				return self.cells[y][x+1]
		else:
			raise ValueError("this is not a valid cell check the range")

	def get_up(self, y, x):
		if self.__is_valid(y,x):
			if y == 0 and x in range(10):
					return 'none'
			else:
				return self.cells[y-1][x]
		else:
			raise ValueError("this is not a valid cell check the range")


	def get_down(self, y, x):
		if self.__is_valid(y, x):
			if y == 9 and x in range(10):
					return 'none'
			else:
				return self.cells[y+1][x]
		else:
			raise ValueError("this is not a valid cell check the range")


	def get_all_neighbour(self, y, x):

		return "{},{},{},{},{},{},{},{}".format(self.get_down(y,x),
												self.get_up(y,x),
												self.get_right(y,x),
												self.get_left(y,x),
												self.get_up_right(y,x),
												self.get_up_left(y,x),
												self.get_down_left(y,x),
												self.get_down_right(y,x))

	def get_living_neighbours(self, y, x):
		#TODO: Implement this. Have it return a number
		return self.get_all_neighbour(y,x).count('0')

	def shuffe_cell(self):
		for y in range(10):
			for x in  range(10):
				current_cell_alive = self.get_cel(y, x)
				living_neighbours = self.get_living_neighbours(y, x)
				#first pattern
				if current_cell_alive and living_neighbours < 2:
					current_cell_alive.update_status(False)
				#second pattern
				if current_cell_alive and living_neighbours in (2,3):
					current_cell_alive.update_status(True)
				#third pattern
				if current_cell_alive and living_neighbours > 3:
					current_cell_alive.update_status(False)
				#last pattern
				if not current_cell_alive and living_neighbours > 2:
					current_cell_alive.update_status(True)





mylist = CellTable()
for _ in range(30):
	os.system('clear')
	mylist.shuffe_cell()
	mylist.get_cells()
	time.sleep(1)
