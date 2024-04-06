import tkinter as tk
from tkinter import ttk
import frontend as fr
import backend as bk


if __name__ == '__main__':
	root = tk.Tk()
	root.title("Beer")
	main_wind = fr.MainWindow(root)
	tab_search = fr.Search(main_wind.tab_control)
	tab_path = fr.Path(main_wind.tab_control)
	main_wind.pack()
	root.mainloop()
