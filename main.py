import tkinter as tk
from tkinter import ttk
import frontend as fr


if __name__ == '__main__':
	root = tk.Tk()
	root.title("Beer")
	tab_control = ttk.Notebook(root)
	tab1 = ttk.Frame(tab_control)
	tab2 = ttk.Frame(tab_control)
	tab_control.add(tab1, text="Search")
	tab_control.add(tab2, text="Path")
	tab_control.pack(expand=1, fill=tk.BOTH)
	tab_search = fr.Search(tab1)
	tab_path = fr.Path(tab2)
	root.mainloop()
