import tkinter as tk
from tkinter import ttk
from api_requests import reddit_news_fetch, nyt_news_fetch, theguardian_news_fetch, google_news_fetch

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

        self.text_widget = tk.Text(mainframe, wrap="word", width=80, height=20)
        self.text_widget.pack(pady=20)

        self.text_widget.pack(pady=20)

    def get_news(self):
        subject = self.entry.get()
        if subject:
            news_data_reddit = reddit_news_fetch(subject)
            news_data_nyt = nyt_news_fetch(subject)
            news_data_tg = theguardian_news_fetch(subject)
            news_data_google = google_news_fetch(subject)
            news_data = news_data_reddit + news_data_nyt + news_data_tg + news_data_google
            self.display_news(news_data)

    def display_news(self, news_data):
       self.text_widget.delete(1.0, tk.END)

       for source, title, link in news_data:
            display_text = f"{title}\nSursa: {source}\nLink: {link}\n\n"
            self.text_widget.insert(tk.END, display_text)
