import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import backend as bk
import threading as thr
import time

PAD = 5


class MainWindow:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Beer")
		self.tab_control = ttk.Notebook(self.root)
		self.search_tab = Search(self.tab_control)

	def pack(self):
		self.tab_control.pack(expand=1, fill=tk.BOTH)

	def mainloop(self):
		self.root.mainloop()


class Search:
	HEADINGS = {'country': 'Страна', 'name': 'Название', 'type': 'Тип', 'paster': 'Пастеризация',
				'filter': 'Фильтрация', 'barcode': 'Штрих-код', 'nach': 'Начальный алкоголь', 'alc': 'Алкоголь',
				'carb': 'Углеводы', 'prot': 'Белки', 'fat': 'Жиры', 'kcal': 'КилоКаллории', 'kjl': 'КилоДжоули',
				'vol': 'Объем', 'ibu': 'IBU', 'ebc': 'EBC', 'container': 'Тара', 'manuf': 'Производитель',
				'link': 'Ссылка', 'image': 'Скан'}
	CONFIG_OF_BEER = (
		'country', 'name', 'type', 'paster', 'filter', 'barcode', 'nach', 'alc', 'carb', 'prot', 'fat', 'kcal', 'kjl',
		'vol', 'ibu', 'ebc', 'container', 'manuf', 'link', 'image')

	def __init__(self, main):
		self.country = (
			'Германия', 'Бельгия', 'Чехия и Словакия', 'Англия', 'Украина', 'СНГ', 'Карибы', 'Прибалтика', 'Европа', 'Азия',
			'Африка', 'Америка', 'Северная Америка', 'Россия')
		self.wind_flag = False
		self.show = ['name', 'type', 'paster']

		self.tab1 = ttk.Frame(main)
		main.add(self.tab1, text='Search')
		self.frm_main = tk.Frame(self.tab1)
		self.frm_main.pack()
		self.frm = tk.Frame(self.frm_main)
		self.frm.pack()
		self.find = tk.Entry(self.frm)
		self.find.grid(row=0, column=0, stick='w', pady=PAD, padx=PAD)
		self.btn_find = tk.Button(self.frm, text='Добавить', command=self._change_flag)
		self.btn_find.grid(row=0, column=1, stick='e', pady=PAD, padx=PAD)

		self.pages_control = ttk.Notebook(self.frm)
		for page in self.country:
			self.page = ttk.Frame(self.pages_control)
			self.pages_control.add(self.page, text=page)
			self.table = ttk.Treeview(self.page, columns=self._reformat_column(), show='headings')
			self.table.grid(row=0, column=0)
			self._show_headings()
		self.pages_control.grid(columnspan=2)

		self.menu_table = tk.Menu(self.table, tearoff=0)
		self.menu_table.add_command(label='Добавить столбец')
		self.menu_table.add_command(label='Удалить столбец')
		self.table.bind('<Button-3>', self._show_menu)

	def set_show(self, string):
		arr = string.split()
		self.show = list(arr)

	def _reformat_column(self):
		return tuple(self.show)

	def _show_headings(self):
		for i in self.show:
			self.table.heading(i, text=self.HEADINGS[i], command=self._show_menu)

	def _show_menu(self, event):
		region = self.table.identify('region', event.x, event.y)
		if region == 'heading':
			self.menu_table.post(event.x_root, event.y_root)

	def _change_flag(self):
		self.wind_flag = True

	def get_response_create_window(self):
		while not self.wind_flag:
			time.sleep(0.001)
		self.wind_flag = False

	# def close_window(self):
	# 	self.wind_flag = False
	# 	self.tab1.destroy()

# Потом мейби напишешь штуку выбора строки


class AddInfo(Search):
	# def _dnd_image(self, event):
	# 	self.path = str(event.data[:-3]) + str(event.data[-3:]).lower()
	# 	if self.path[-3:] == 'jpg' or self.path[-3:] == 'png':
	# 		# print(os.path.abspath(self.path))
	# 		self.image = Image.open(os.path.abspath(self.path))
	# 		self.photo = ImageTk.PhotoImage(self.image)
	# 		self.entr_img.delete('all')
	# 		self.entr_img.create_image(10, 10, anchor='nw', image=self.photo)

	def __init__(self):
		self.data_flag = False
		self.image = None
		self.root_add = tk.Toplevel()
		self.root_add.resizable(False, False)
		self.root_add.title('Добавление данных')
		self.root_add.geometry('1000x815')
		self.entr_get = []
		self.part_len = int(len(self.CONFIG_OF_BEER[:-2]) / 2)
		for text, i in zip(self.CONFIG_OF_BEER[:self.part_len], range(self.part_len)):
			self.txt = tk.Label(self.root_add, text=f'{self.HEADINGS[text]}')
			self.txt.grid(sticky='w', column=0, row=i, padx=PAD, pady=PAD)
			self.entr = tk.Entry(self.root_add, width=50)
			self.entr_get.append(self.entr)
			self.entr.grid(column=1, row=i, padx=PAD, pady=PAD)
		for text, i in zip(self.CONFIG_OF_BEER[self.part_len:], range(self.part_len)):
			self.txt = tk.Label(self.root_add, text=f'{self.HEADINGS[text]}')
			self.txt.grid(sticky='w', column=2, row=i, padx=PAD, pady=PAD)
			self.entr = tk.Entry(self.root_add, width=50)
			self.entr_get.append(self.entr)
			self.entr.grid(column=3, row=i, padx=PAD, pady=PAD)
		self.txt_link = tk.Label(self.root_add, text='Ссылка')
		self.txt_link.grid(sticky='w', column=0, padx=PAD, pady=PAD)
		self.entr_link = tk.Entry(self.root_add, width=120)
		self.entr_link.grid(column=1, columnspan=3, row=self.txt_link.grid_info()['row'], padx=PAD, pady=PAD)
		self.txt_img = tk.Label(self.root_add, text='Скан')
		self.txt_img.grid(sticky='e', row=len(self.CONFIG_OF_BEER) * 2, padx=PAD, pady=PAD)
		self.entr_img = tk.Canvas(self.root_add, bg='white', width=450, height=450)
		self.entr_img.grid(column=1, row=len(self.CONFIG_OF_BEER) * 2, columnspan=3, padx=PAD, pady=PAD)
		self.btn_img = tk.Button(self.root_add, text='Добавить', command=self._find_image)
		self.btn_img.grid(row=len(self.CONFIG_OF_BEER) * 2, column=3, sticky='e')
		self.btn_appl = tk.Button(self.root_add, text='Подтвердить', command=self._change_flag)
		self.btn_appl.grid(column=1, row=len(self.CONFIG_OF_BEER) * 2 + 1, columnspan=3, padx=PAD, pady=PAD)

		# self.root_add.protocol('WM_DELETE_WINDOW', self._close_window)

	def _change_flag(self):
		self.data_flag = True

	def get_response_data(self):
		while not self.data_flag:
			time.sleep(0.001)

	def _find_image(self):
		filepath = fd.askopenfilename()
		if filepath[-3:] == 'jpg' or filepath[-3:] == 'png':
			self.image = Image.open(os.path.abspath(filepath))
			photo = ImageTk.PhotoImage(self.image)
			self.entr_img.delete('all')
			self.entr_img.create_image(0, 0, anchor='nw', image=photo)

	def _format_data(self, arr):
		# arr = [None if i == '' else i for i in arr]
		for i in range(len(arr)):
			if arr[i] != '':
				arr[i] = arr[i].strip(' ')

		for i in range(2, 5):
			if arr[i]:
				arr[i] = arr[i].capitalize()
		return arr

	def _check(self, arr):
		print(arr, end=' ')
		print(' _check')
		standart_contry = ('Германия', 'Бельгия', 'Чехия и Словакия', 'Англия', 'Украина', 'СНГ', 'Карибы', 'Прибалтика', 'Европа', 'Азия',
			'Африка', 'Америка', 'Северная Америка', 'Россия')
		standart_type = ('Светлое', 'Темное', 'Тёмное', 'Полусветлое', 'Полутёмное', 'Полутемное', '')
		standart_bool = ('Да', 'Нет', '')
		if arr[0] == '':
			mb.showerror('Error', 'Вы не ввели название страны')
		if arr[0] not in standart_contry:
			mb.showerror('Error', 'Такой страны нет в списке или проверьте опечатки')
		if arr[2] not in standart_type:
			mb.showerror('Error', 'Неправильный формат поля "тип пива"')
			return False
		if arr[3] not in standart_bool:
			mb.showerror('Error', 'Неправильный формат поля "пастеризация"')
			return False
		if arr[4] not in standart_bool:
			mb.showerror('Error', 'Неправильный формат поля "фильтрация"')
			return False
		if arr[5] != '':
			if len(arr[5]) != 13 or len(arr[5]) != 8:
				mb.showerror('Error', 'Неправильный формат поля "штрих-код"')
				return False
		return True

	def get_data_from_entrances(self):
		data = []					# Сохраняет оно все в строках поэтому давай так и оставим
		for i in self.entr_get[:-1]:
			data.append(i.get())
		data = self._format_data(data)

		if self.entr_link.get() != '':
			data.append(self.entr_link.get())
		else:
			data.append('')

		if self.image is not None:
			data.append(self.image)
		else:
			data.append('')

		print(data)
		if self._check(data):
			self.wind_flag = False
			self.data_flag = False
			return tuple(data)

class Path:
	def __init__(self, main):
		self.tab2 = ttk.Frame(main)
		main.add(self.tab2, text='Path')
		self.lb = tk.Label(self.tab2, text='Вставьте путь расположения файла БД')
		self.lb.grid(row=0, column=0, padx=PAD, pady=PAD)
		self.entry = tk.Entry(self.tab2, width=50)
		self.entry.grid(row=0, column=1, padx=PAD, pady=PAD)
		self.btn_add = tk.Button(self.tab2, text='Внести изменения')
		self.btn_add.grid(row=0, column=2, padx=PAD, pady=PAD)

	def set_path(self):
		pass
