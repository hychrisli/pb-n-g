from datetime import date
from datetime import timedelta
from enum import Enum
from 

BOOK_LOAD_DAYS = 10


class BookFormat(Enum):
    hardcover = "hardcover"
    paperback = "paperback"
    audiobook = "audiobook"
    ebook = "ebook"
    newspaper = "newspaper"
    magazine = "magazine"
    journal = "journal"

class BookStatus(Enum):
    available = "available"
    reserved = "reserved"
    loaned = "loaned"
    lost = "lost"


class Book:

    def __init__(self, title, isbn, subject, publisher, language, pages_num):
        self.__title = title
        self.__isbn = isbn
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__pages_num = pages_num
    
    def get_title(self):
        return self.__title


"""
    barcode scan -> find book in database -> return entity object -> data transformation object (dto) -> data access object (dao)
"""
class BookItem(Book):

    def __init__(
        self,
        id: str, 
        barcode: str,
        borrowed_date: date,
        due_date: date,
        price: float,
        book_format: BookFormat,
        book_status: BookStatus,
        purchase_date: date,
        publication_date: date,
    ):
        self.__barcode = barcode
        self.__borrowed_date = borrowe_date
        self.__due_date = due_date
        self.__price = price
        self.__book_format = book_format
        self.__book_status = book_status
        self.__purchase_date = purchase_date
        self.__publication_date = publication_date


    def check_out(self):
        self.__borrowed_date = date.today()
        self.__due_date = self.__borrow_date + timedelta(BOOK_LOAD_DAYS)
        self.__book_status = BookStatus.loaned


    def reserve(self):
        self.__book_status = BookStatus.reserved

    
    def check_in(self):
        self.__book_status = BookStatus.available
        self.__borrowed_date = None
        self.__due_date = None

class BookReservation:

    def __init__(self, ...):

    

class Author:
    
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
    
    def get_name(self):
        return self.__name