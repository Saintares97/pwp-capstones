class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}


    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email address for user {} has been changed to {}.".format(self.name, self.email))
        
    def __repr__(self):
        return "User {} with email address {} has read {} books.".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN for the book titled {} has been changed to {}.".format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating is not None:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

        
    def __eq__(self, other_book):
        if self.title == other_book.tittle and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return self.title
    

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
    
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book]= 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        read_count = 0
        most_read = None
        for book in self.books:
            times_read = self.books[book]
            if times_read > read_count:
                read_count = times_read
                most_read = book
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated = None
        for book in self.books:
            avrg_rating = book.get_average_rating()
            if avrg_rating > highest_rating:
                highest_rating = avrg_rating
                highest_rated = book
            return highest_rated

    def most_positive_user(self):
        p_rating = 0
        m_positive = None
        for user in self.users.values():
            user_avrg = user.get_average_rating()
            if user_avrg > p_rating:
                p_rating = user_avrg
                m_positive = user
        return m_positive
