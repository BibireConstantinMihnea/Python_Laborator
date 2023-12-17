import tkinter as tk
from tkinter import ttk
from api_requests import reddit_news_fetch, nyt_news_fetch, theguardian_news_fetch, google_news_fetch
import webbrowser
from tkinter import messagebox

class NewsFeed:
    def __init__(self, mainframe):
        self.mainframe = mainframe
        self.mainframe.title("News Feed App")

        self.label = ttk.Label(mainframe, text="Enter a subject: ")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(mainframe, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.get_news())

        self.button = ttk.Button(mainframe, text="Search News", command=self.get_news)
        self.button.pack(pady=10)

        self.scrollbar = ttk.Scrollbar(mainframe)
        self.scrollbar.pack(pady=20, side=tk.RIGHT, fill=tk.Y)

        self.text_widget = tk.Text(mainframe, wrap="word", width=105, height=40, yscrollcommand=self.scrollbar.set, state="disabled")
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
        else:
            messagebox.showinfo("No Subject", "Please enter a subject before searching.")

    def display_news(self, news_data):
       self.text_widget.configure(state="normal")
       self.text_widget.delete(1.0, tk.END)

       for source, title, link in news_data:
            display_text = f"{title}\nSursa: {source}\nLink: "
            self.text_widget.insert(tk.END, display_text)

            self.text_widget.tag_configure(f"{link}", foreground='#0041C2', underline='True')

            start = self.text_widget.index(tk.END)
            self.text_widget.insert(tk.END, link, f"{link}")
            end = self.text_widget.index(tk.END)

            self.text_widget.tag_add(f"{link}", start, end)
            self.text_widget.tag_bind(f"{link}", "<Button-1>", lambda event, url=link: self.open_link(event, url))
            self.text_widget.insert(tk.END, "\n\n")
        
       self.text_widget.configure(state="disabled")

    def open_link(self, event, url):
        try:
            webbrowser.open_new(url)

        except webbrowser.Error as e:
            messagebox.showerror(f"Error", "Link cannot be accessed: {e}")
