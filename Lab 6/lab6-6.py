from datetime import date, timedelta

class LibraryItem:
    def __init__(self, name, available = True):
        self.name = name
        self.available = available
        self.check_out_date = None
        self.return_date = None

    def check_out(self):
        if self.available:
            self.available = False
            self.check_out_date = date.today()
            self.return_date = self.check_out_date + timedelta(days=14)
            print(f"Item {self.name} has been checked out. Due date {self.return_date}.")
        
        else : print(f"Item {self.name} is not available.")

    def return_item(self):
        if not self.available:
            self.available = True
            self.check_out_date = None
            self.due_date = None
            print(f"{self.name} has been returned.")
        else:
            print(f"{self.name} is already available.")

    def display_info(self):
        print(f"Item name: {self.name}")
        status = "Available" if self.available else "Checked-out"
        print(f"Status: {status}")

class Book(LibraryItem):
    def __init__(self, name, author, available=True):
        super().__init__(name, available)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class DVD(LibraryItem):
    def __init__(self, name, director, available=True):
        super().__init__(name, available)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")

class Magazine(LibraryItem):
    def __init__(self, name, edition, available=True):
        super().__init__(name, available)
        self.edition = edition

    def display_info(self):
        super().display_info()
        print(f"Edition: {self.edition}")


book = Book("Amintiri din copilarie", "Ion Creanga")
book.display_info()
book.check_out()
print("\n")
dvd = DVD("Jaws", "Steven Spielberg")
dvd.display_info()
dvd.check_out()
print("\n")
magazine = Magazine("National Geographic", 242)
magazine.display_info()
magazine.check_out()
magazine.return_item()