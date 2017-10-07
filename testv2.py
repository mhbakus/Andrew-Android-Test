import random
#class cell for represent a cell
class Cell:
	def __init__(self, statut):
		self.statut = statut

	def __repr__(self):
		return '{}'.format(self.statut)
	def get_cell(self):
		return self.statut

	def update_status(self, status):
		self.statut = status


#class celltable for represent a table of cells
class CellTable:
	def __init__(self, cellist = []):
		self.cells = cellist

	def add_cell(self, cell = []):
		self.cells.append(cell)

	def get_cells(self):
		for cell in self.cells:
			print(cell)

	def get_cel(self, y, x):
		return self.cells[y][x]

	def get_up_left(self, y, x):
		if y == 0:
			return 'none'
		else:
			return self.cells[y-1][x-1]

	def get_up_right(self, y, x):
		if y == 0 or x == 9:
			return 'none'
		else:
			return self.cells[y-1][x+1]

	def get_down_left(self, y, x):
		if y == 9:
			return 'none'
		else:
			return self.cells[y+1][x-1]

	def get_down_right(self, y, x):
		if y == 9 or x == 9:
			return 'none'
		else:
			return self.cells[y+1][x+1]

	def get_left(self, y, x):
		if x == 0:
			return 'none'
		else:
			return self.cells[y][x-1]

	def get_right(self, y, x):
		if x == 9:
			return 'none'
		else:
			return self.cells[y][x+1]

	def get_up(self, y, x):
		if y == 0:
			return 'none'
		else:
			return self.cells[y-1][x]

	def get_down(self, y, x):
		if y == 9:
			return 'none'
		else:
			return self.cells[y+1][x]

	def get_all_neighbour(self, y, x):

		return "{},{},{},{},{},{},{},{}".format(self.get_down(y,x),
												self.get_up(y,x),
												self.get_right(y,x),
												self.get_left(y,x),
												self.get_up_right(y,x),
												self.get_up_left(y,x),
												self.get_down_left(y,x),
												self.get_down_right(y,x))





choix = ('live','death')
my_cell_list = CellTable()

for _ in range(10):
	dumy_list = []
	for _ in range(10):
		dumy_list.append(Cell(random.choice(choix)))
	my_cell_list.add_cell(dumy_list)


# for y in range(10):
# 	for x in range(10):
# 		print(my_cell_list.get_cel(y,x).update_status('alive'))
# 		print(my_cell_list.get_cel(y,x))

my_cell_list.get_cells()
for _ in range(7):
	for y in range(10):
		for x in range(10):
			neighbourg = my_cell_list.get_all_neighbour(y,x)
			alive = neighbourg.count('live')
			death = neighbourg.count('death')

			#now let check the first pattern
			if my_cell_list.get_cel(y,x) == 'live' and alive < 2:
				my_cell_list.get_cel(y,x).statut = 'death'
			#second pattern
			if my_cell_list.get_cel(y,x) == 'live' and alive == 2 or alive == 3:
				my_cell_list.get_cel(y,x).statut = 'live'
			#third patter
			if my_cell_list.get_cel(y,x) == 'live' and alive > 3:
				my_cell_list.get_cel(y,x).statut = 'death'
			#last pattern
			if my_cell_list.get_cel(y,x) == 'death' and alive > 3:
				my_cell_list.get_cel(y,x).statut = 'live'


print('\n')
my_cell_list.get_cells()