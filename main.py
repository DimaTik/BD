import tkinter as tk
from tkinter import ttk
import frontend as gui
import backend as bk
import threading as thr
import time


def get_set_data():
	while True:
		main_wind.search_tab.get_response_create_window() 	# Бяка(
		add_wind = gui.AddInfo()
		add_wind.get_response_data()
		data.set_data(add_wind.get_data())
		add_wind.show_successful_window()


if __name__ == '__main__':
	main_wind = gui.MainWindow()
	main_wind.pack()
	data = bk.Data()
	for i in main_wind.search_tab.countries_list:
		main_wind.search_tab.set_data_for_show(data.get_data(i), i)
	thread_add_data = thr.Thread(target=get_set_data, daemon=True).start()
	main_wind.mainloop()
