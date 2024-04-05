import tkinter as tk
from tkinter import ttk


PAD = 5


class Search:
	HEADINGS = {'id': 'Номер', 'cost': 'Цена', 'age': 'Год'}
	show = ['id', 'cost', 'age']

	def __init__(self, main):
		self.find = tk.Entry(main)
		self.find.grid(row=0, column=0, stick='w', padx=PAD, pady=PAD)
		self.btn_find = tk.Button(main, text='Добавить')
		self.btn_find.grid(row=0, column=1, stick='e', padx=PAD, pady=PAD)
		self.table = ttk.Treeview(main, columns=self._reformat_column(), show='headings')
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
		self.lb = tk.Label(main, text='Вставьте путь расположения файла БД')
		self.lb.grid(row=0, column=0, padx=PAD, pady=PAD)
		self.entry = tk.Entry(main, width=50)
		self.entry.grid(row=0, column=1, padx=PAD, pady=PAD)
		self.btn_add = tk.Button(text='Внести изменения')

	def set_entry(self):
		pass
