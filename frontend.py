import tkinter as tk
from tkinter import ttk
import tkinterdnd2 as tkdnd

PAD = 5


class MainWindow:
	def __init__(self, main):
		self.tab_control = ttk.Notebook(main)

	def pack(self):
		self.tab_control.pack(expand=1, fill=tk.BOTH)


class Search:
	HEADINGS = {'country': 'Страна', 'name': 'Название', 'type': 'Тип', 'paster': 'Пастеризация', 'filter': 'Фильтрация', 'barcode': 'Штрих-код', 'nach': 'Начальный алкоголь', 'alc': 'Алкоголь', 'carb': 'Углеводы', 'prot': 'Белки', 'fat': 'Жиры', 'kcal': 'КилоКаллории', 'kjl': 'КилоДжоули', 'vol': 'Объем', 'ibu': 'IBU', 'ebc': 'EBC', 'container': 'Тара', 'manuf': 'Производитель', 'link': 'Ссылка', 'image': 'Скан'}
	show = ['name', 'type', 'paster']
	list = ('country', 'name', 'type', 'paster', 'filter', 'barcode', 'nach', 'alc', 'carb', 'prot', 'fat', 'kcal', 'kjl', 'vol', 'ibu', 'ebc', 'container', 'manuf', 'link', 'image')
	country = ('Германия', 'Бельгия', 'Чехия и Словакия', 'Англия', 'Украина', 'СНГ', 'Карибы', 'Прибалтика', 'Европа', 'Азия', 'Африка', 'Америка', 'Северная Америка', 'Россия')

	def __init__(self, main):
		self.tab1 = ttk.Frame(main)
		main.add(self.tab1, text='Search')
		self.frm_main = tk.Frame(self.tab1)
		self.frm_main.pack()
		self.frm = tk.Frame(self.frm_main)
		self.frm.pack()
		self.find = tk.Entry(self.frm)
		self.find.grid(row=0, column=0, stick='w', pady=PAD, padx=PAD)
		self.btn_find = tk.Button(self.frm, text='Добавить', command=self._add_record)
		self.btn_find.grid(row=0, column=1, stick='e', pady=PAD, padx=PAD)

		self.pages_control = ttk.Notebook(self.frm)
		for page in self.country:
			self.page = ttk.Frame(self.pages_control)
			self.pages_control.add(self.page, text=page)
			self.table = ttk.Treeview(self.page, columns=self._reformat_column(), show='headings')
			self.table.grid(row=0, column=0)
			self._show_headings()
		self.pages_control.grid(columnspan=2)
		# self.pages_control.pack(expand=1, fill=tk.BOTH)

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

	def _dnd_image(self):
		pass

	def _add_record(self):
		self.list_entr = list(map(lambda x: 'entr_' + x, self.list[:-2]))
		self.list_txt = list(map(lambda x: 'txt_' + x, self.list[:-2]))
		self.root_rec = tkdnd.Tk()
		self.part_len = int(len(self.list_txt)/2)
		self.root_rec.resizable(False, False)
		self.root_rec.title('Добавление данных')
		self.root_rec.geometry(f'1000x850')
		for txt, entr, text, i in zip(self.list_txt[:self.part_len], self.list_entr[:self.part_len], self.list[:self.part_len], range(self.part_len)):
			self.txt = tk.Label(self.root_rec, text=f'{self.HEADINGS[text]}')
			self.txt.grid(sticky='w', column=0, row=i, padx=PAD, pady=PAD)
			self.entr = tk.Entry(self.root_rec, width=50)
			self.entr.grid(column=1, row=i, padx=PAD, pady=PAD)
		for txt, entr, text, i in zip(self.list_txt[self.part_len:], self.list_entr[self.part_len:], self.list[self.part_len:], range(self.part_len)):
			self.txt = tk.Label(self.root_rec, text=f'{self.HEADINGS[text]}')
			self.txt.grid(sticky='w', column=2, row=i, padx=PAD, pady=PAD)
			self.entr = tk.Entry(self.root_rec, width=50)
			self.entr.grid(column=3, row=i, padx=PAD, pady=PAD)
		self.txt_link = tk.Label(self.root_rec, text='Ссылка')
		self.txt_link.grid(sticky='w', column=0, padx=PAD, pady=PAD)
		self.entr_link = tk.Entry(self.root_rec, width=120)
		self.entr_link.grid(column=1, columnspan=3, row=self.txt_link.grid_info()['row'], padx=PAD, pady=PAD)
		self.txt_img = tk.Label(self.root_rec, text='Скан')
		self.txt_img.grid(sticky='w', row=len(self.list)*2, column=0, padx=PAD, pady=PAD)
		self.frm_img = tk.Frame(self.root_rec)
		self.frm_img.grid(column=1, columnspan=3, row=len(self.list)*2)
		self.entr_img = tk.Text(self.frm_img, height=30, width=90)
		# self.entr_img = tk.Entry(self.frm_img, width=50)
		self.entr_img.grid(column=1, row=len(self.list)*2, padx=PAD, pady=PAD)
		# self.entr_img.drop_target_register()
		self.btn_appl = tk.Button(self.root_rec, text='Подтвердить')
		self.btn_appl.grid(column=2, row=len(self.list)*2+1, padx=PAD, pady=PAD)
		# self.btn_canc = tk.Button(self.root_rec, text='Отмена')
		# self.btn_canc.grid(column=1, row=len(self.list)*2+1, padx=PAD, pady=PAD)


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
