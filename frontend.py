import tkinter as tk
from tkinter import ttk


PAD = 5


class MainWindow:
	def __init__(self, main):
		self.tab_control = ttk.Notebook(main)

	def pack(self):
		self.tab_control.pack(expand=1, fill=tk.BOTH)


class Search:
	HEADINGS = {'id': 'Номер', 'cost': 'Цена', 'age': 'Год'}
	show = ['id', 'cost', 'age']

	def __init__(self, main):
		self.tab1 = ttk.Frame(main)
		main.add(self.tab1, text='Search')
		self.find = tk.Entry(self.tab1)
		self.find.grid(row=0, column=0, stick='w', padx=PAD, pady=PAD)
		self.btn_find = tk.Button(self.tab1, text='Добавить')
		self.btn_find.grid(row=0, column=1, stick='e', padx=PAD, pady=PAD)
		self.table = ttk.Treeview(self.tab1, columns=self._reformat_column(), show='headings')
		self.table.grid(row=2, column=0, columnspan=2)
		self._show_headings()

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
	# Потом мейби напишешь штуку выбора строки


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

	def set_entry(self):
		pass
