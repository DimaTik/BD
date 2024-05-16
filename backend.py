import sqlite3 as sq

with sq.connect('db.db') as con:
	cur = con.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS Германия(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		type TEXT,
		paster TEXT,
		filter TEXT,
		barcode TEXT,
		nach TEXT,
		alc TEXT,
		carb TEXT,
		fat TEXT,
		kcal TEXT,
		kjl TEXT,
		vol TEXT,
		ibu TEXT,
		ebc TEXT,
		container TEXT,
		manuf TEXT,
		link TEXT,
		image BLOB
)""")


class Data:
	columns = (
		'country', 'name', 'type', 'paster', 'filter', 'barcode', 'nach', 'alc', 'carb', 'prot', 'fat', 'kcal', 'kjl',
		'vol', 'ibu', 'ebc', 'container', 'manuf', 'link', 'image')

	def _column(self, arr):
		temp = []
		for i in range(1, len(arr)):
			if arr[i]:
				temp.append(self.columns[i])
		return tuple(temp)

	def _to_string(self, arr):
		temp = []
		for i in arr[1:]:
			if i != '':
				temp.append(i)
		string = '' ''.join(temp)
		return string

	def set_data(self, arr):
		col = self._column(arr)
		write_arr = self._to_string(arr)
		print(write_arr)
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			cur.execute(f"INSERT INTO {arr[0]} ({col}) VALUES({write_arr})")
		print('write data finish')

	def get_data(self):
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			arr = cur.execute("SELECT * FROM Германия").fetchall()
			return arr

	# def _get_types(self):
	# 	self.list = []
	# 	with sq.connect('BD.db') as self.con:
	# 		self.cur = con.cursor()
	# 		self.temp = self.cur.execute('''PRAGMA table_info('Germany')''')
	# 		self.temp = self.cur.fetchall()
	# 		for i in range(len(self.temp)):
	# 			self.list.append(self.temp[i][2])
	# 		return self.list
