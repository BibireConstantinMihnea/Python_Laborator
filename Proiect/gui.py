import tkinter as tk
from tkinter import ttk
from api_requests import reddit_news_fetch

class NewsFeed:
    def __init__(self, mainframe):
        self.mainframe = mainframe
        self.mainframe.title("News Feed App")

        self.label = ttk.Label(mainframe, text="Introduceti subiectul dorit: ")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(mainframe)
        self.entry.pack(pady=10)

        self.button = ttk.Button(mainframe, text="Cautare", command=self.get_news)
        self.button.pack(pady=10)

        self.tree = ttk.Treeview(mainframe, columns=("Source", "Title", "Link"))
        self.tree.heading("#0", text="Nr.")
        self.tree.heading("Source", text="Sursa")
        self.tree.heading("Title", text="Titlu")
        self.tree.heading("Link", text="Link")
        self.tree.pack(pady=20)

    def get_news(self):
        subject = self.entry.get()
        if subject:
            news_data = reddit_news_fetch(subject)
            self.display_news(news_data)

    def display_news(self, news_data):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for news in news_data:
            self.tree.insert("", "end", values=news)
