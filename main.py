import tkinter as tk
from tkinter import ttk
import frontend as fr
import backend as bk


if __name__ == '__main__':
	main_wind = fr.MainWindow()
	tab_search = fr.Search(main_wind.tab_control)
	tab_path = fr.Path(main_wind.tab_control)
	main_wind.pack()
	main_wind.mainloop()
