import tkinter as tk
from gui import NewsFeed

mainframe = tk.Tk()
mainframe.geometry("850x650")
app = NewsFeed(mainframe)
mainframe.mainloop() 