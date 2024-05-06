import sqlite3 as sq

with sq.connect('db.db') as con:
	cur = con.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS Германия(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		country TEXT,
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
	def set_data(self, arr):
		with sq.connect('db.db') as self.con:
			self.cur = con.cursor()
			self.cur.execute(f'''INSERT {arr[0]} VALUES {arr[1:]}''')
		print('write data')

	def show(self):
		with sq.connect('db.db') as self.con:
			self.cur = con.cursor()
			self.arr = self.cur.execute('''SELECT * FROM Германия''')
			self.arr = self.cur.fetchall()
			return self.arr

	# def _get_types(self):
	# 	self.list = []
	# 	with sq.connect('BD.db') as self.con:
	# 		self.cur = con.cursor()
	# 		self.temp = self.cur.execute('''PRAGMA table_info('Germany')''')
	# 		self.temp = self.cur.fetchall()
	# 		for i in range(len(self.temp)):
	# 			self.list.append(self.temp[i][2])
	# 		return self.list
