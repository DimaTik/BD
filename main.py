import tkinter as tk
from tkinter import ttk
import frontend as gui
import backend as bk
import threading as thr
import time


def get_set_data():
	while True:
		main_wind.search_tab.get_response_create_window() 	# Бяка(
		search_tab = gui.AddInfo()
		search_tab.get_response_data()
		data.set_data(search_tab.get_data_from_entrances())


if __name__ == '__main__':
	main_wind = gui.MainWindow()
	main_wind.pack()
	data = bk.Data()
	thread = thr.Thread(target=get_set_data, daemon=True)
	thread.start()
	main_wind.mainloop()
