import sqlite3 as sq
import time

with sq.connect('db.db') as con:
	cur = con.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS Чехия_и_Словакия(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		type TEXT,
		paster TEXT,
		filter TEXT,
		barcode TEXT,
		nach TEXT,
		alc TEXT,
		carb TEXT,
		prot TEXT,
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

	# def __init__(self):
	# 	self.flag_successful = False

	def _column(self, arr):
		temp = []
		for i in range(1, len(arr)):
			if arr[i]:
				temp.append(self.columns[i])
		if len(temp) > 1:
			return tuple(temp)
		else:
			return f"('{temp[0]}')"

	def _format_array(self, arr):
		temp = []
		for i in arr[1:]:
			if i != '':
				temp.append(i)
		if len(temp) > 1:
			return tuple(temp)
		else:
			return f"('{temp[0]}')"

	def _vol_of_val(self, arr):
		temp = ''
		for i in range(len(arr)):
			temp += '?,'
		return temp[:-1]

	# def _gap_spaces(self, string):
	# 	return string.replace(' ', '_')

	# А че мы просто не записываем массив с пустотой?

	def set_data(self, arr):
		col = str(self._column(arr))
		print(col)
		write_arr = self._format_array(arr)
		print(write_arr)
		# name = self._gap_spaces(arr[0])
		# print(name)
		response = f"INSERT INTO {arr[0]} {col} VALUES({self._vol_of_val(write_arr)})"
		print(response)
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			cur.execute(response, write_arr)
		# self.flag_successful = True
		print('write data finish')

	def get_data(self, country):
		with sq.connect('db.db', check_same_thread=False) as con:
			cur = con.cursor()
			arr = cur.execute(f"SELECT * FROM {country}").fetchall()
			return tuple(arr)

	# def get_response_successful(self):
	# 	while not self.flag_successful:
	# 		time.sleep(0.001)
	# 	self.flag_successful = False
