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
		if len(temp) > 1:
			return tuple(temp)
		else:
			return f"('{temp[0]}')"

			# INSERT INTO Германия (name) VALUES(чдмщш2й) !!!!!!!!!!!!!

	def _format_array(self, arr):
		temp = []
		for i in arr[1:]:
			if i != '':
				temp.append(i)
		if len(temp) > 1:
			return tuple(temp)
		else:
			return f"('{temp[0]}')"

	# А че мы просто не записываем массив с пустотой?

	def set_data(self, arr):
		col = str(self._column(arr))
		# print(col)
		write_arr = self._format_array(arr)
		# print(write_arr)
		response = f"INSERT INTO {arr[0]} {col} VALUES{write_arr}"
		# print(response)
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			cur.execute(response)
		print('write data finish')

	def get_data(self):
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			arr = cur.execute("SELECT * FROM Германия").fetchall()
			return arr
