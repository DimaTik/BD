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
		if data.get_successful_set_data():
			add_wind.show_successful_window()


def close_program():
	while True:
		main_wind.get_response_close_program()
		data.set_column_order(main_wind.search_tab.get_column_order())
		if data.get_successful_close_program():
			break


if __name__ == '__main__':
	data = bk.Data()
	order_column = data.get_column_order()
	main_wind = gui.MainWindow(order_column)
	main_wind.pack()

	# main_wind.search_tab.set_column_order(data.get_column_order())
	countries = main_wind.search_tab.get_countries()
	for i in countries:
		main_wind.search_tab.set_data_for_show(data.get_data(i), i)
	thread_add_data = thr.Thread(target=get_set_data, daemon=True).start()
	thread_close_program = thr.Thread(target=close_program).start()
	main_wind.mainloop()
