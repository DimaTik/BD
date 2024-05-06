import tkinter as tk
from tkinter import ttk
import frontend as gui
import backend as bk
import threading as thr
import time


def get_set_data():
	while True:
		wind_add_data.get_response_data()
		data.set_data(wind_add_data.get_data_from_entrances())


if __name__ == '__main__':
	main_wind = gui.MainWindow()
	tab_search = gui.Search()
	tab_search.create_window(main_wind.tab_control)
	tab_path = gui.Path()
	tab_path.create_window(main_wind.tab_control)
	main_wind.pack()
	data = bk.Data()
	wind_add_data = gui.AddInfo()
	thr.Thread(target=get_set_data, daemon=True).start()
	main_wind.mainloop()
