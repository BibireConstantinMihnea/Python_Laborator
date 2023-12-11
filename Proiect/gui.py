import tkinter as tk
from tkinter import ttk

class NewsFeed:
    def __init__(self, mainframe):
        self.mainframe = mainframe
        self.mainframe.title("News Feed App")

        self.label = ttk.Label(mainframe, text="Introduceti subiectul dorit: ")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(mainframe)
        self.entry.pack(pady=10)

        self.button = ttk.Button(mainframe, text="Cautare")
        self.button.pack(pady=10)

        self.tree = ttk.Treeview(mainframe, columns=("Source", "Title", "Link"))
        self.tree.heading("#0", text="Nr.")
        self.tree.heading("Source", text="Sursa")
        self.tree.heading("Title", text="Titlu")
        self.tree.heading("Link", text="Link")
        self.tree.pack(pady=20)
