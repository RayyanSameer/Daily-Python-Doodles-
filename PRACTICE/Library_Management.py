import json 
import os 

book_file = "books.json"
members_file = "members.json"
transactions = 'transactions.json'

# Book class
class Book:
    def __init__(self, title, book_id, author, genre, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author 
        self.genre = genre
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False   
            print(f'You have borrowed "{self.title}"')
        else:
            print(f"{self.title} isn't available")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned {self.title}")
        else:
            print("Book is already available")


# Member Class 
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


     


class Transaction:
    def __init__(self, member_id, book_id, action):
        self.member_id = member_id
        self.book_id = book_id
        self.action = action


class Library:
    def __init__(self):
        self.books = self.load_data(book_file)
        self.members = self.load_data(members_file)  # Fixed: was 'member'
        self.transactions = self.load_data(transactions)

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
        return {}

    def save_data(self, filename, data):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, genre):
        book_id = str(len(self.books) + 1)
        book = Book(title, book_id, author, genre)
        self.books[book_id] = vars(book)
        print(f"📚 Added book: {title}")
        self.save_data(book_file, self.books)

    def view_books(self):
        if not self.books:
            print("No books available")
        else:
            for b in self.books.values():
                status = "Available" if b["available"] else "Issued"
                print(f"{b['book_id']}. {b['title']} - {b['author']} ({status})")

#Member Methods 
    def add_book(self,title,author,genre) :
        book_id = str(len(sel))  