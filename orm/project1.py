from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base,relationship
#database connection
engine=create_engine('sqlite:///library_track.db')
Base=declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Category(Base):
    __tablename__='categories'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    books=relationship('book', back_populates='category')
class Book(Base):
    __tablename__='books'
    id=Column(Integer, primary_key=True)
    title=Column(String)
    author=Column(String)
    category_id=Column(Integer, ForeignKey('categories.id'))
    categories=relationship('Category', back_populates='books')
    borrows=relationship('Borrow', back_populates='books')
class Borrow(Base):
    __tablename__='borrows'
    id=Column(Integer, primary_key=True)
    book_id=Column(Integer, ForeignKey('books.id'))
    borrower_name=Column(String)
    borrow_date=Column(String)
    return_date=Column(String)
    books=relationship('Book', back_populates='borrows')
class Limit(Base):
    __tablename__='limits'
    id=Column(Integer, primary_key=True)
    borrower_name=Column(String)
    month=Column(String)
    max_books=Column(Integer)

def add_catrgory():
    name = input("Enter category name: ")
    category = Category(name=name)
    session.add(category)
    session.commit()
    print("category added")
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    category_id = int(input("Enter category ID: "))
    # create book object
    session.add(Book(title=title, author=author, category_id=category_id))
    session.commit()
def borrow_book():
    book_id = int(input("Enter book ID: "))
    borrower_name = input("Enter borrower name: ")
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    return_date = input("Enter return date (YYYY-MM-DD): ")
    session.add(Borrow(book_id=book_id, borrower_name=borrower_name, borrow_date=borrow_date, return_date=return_date))
    session.commit()
    print("Book borrowed successfully")
def update_borrow():
    borrow_id = int(input("Enter borrow ID to update: "))
    borrow = session.query(Borrow).filter_by(id=borrow_id).first()
    if borrow:
        session.delete(borrow)
        session.commit()
        print("Borrow record deleted successfully")
    else:
        print("Borrow record not found")
def set_limit():
    borrower_name = input("Enter borrower name: ")
    month = input("Enter month (YYYY-MM): ")
    max_books = int(input("Enter maximum number of books allowed: "))
    session.add(Limit(borrower_name=borrower_name, month=month, max_books=max_books))
    session.commit()
    print("Limit set successfully")
Base.metadata.create_all(engine)
def search_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    borrows = session.query(Borrow).filter_by(borrow_date=date).all()
    for borrow in borrows:
        print(f"Borrow ID: {borrow.id}, Book ID: {borrow.book_id}, Borrower Name: {borrow.borrower_name}, Borrow Date: {borrow.borrow_date}, Return Date: {borrow.return_date}")
def category_summary():
    categories = session.query(Category).all()
    for category in categories:
        print(f"Category ID: {category.id}, Name: {category.name}, Number of Books: {len(category.books)}")
def main():
    while True:
        print("1. Add Category")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Update Borrow")
        print("5. Set Borrow Limit")
        print("6. Search by Date")
        print("7. Category Summary")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_catrgory()
        elif choice == '2':
            add_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            update_borrow()
        elif choice == '5':
            set_limit()
        elif choice == '6':
            search_by_date()
        elif choice == '7':
            category_summary()
        elif choice == '8':
            break
        else:
            print("Invalid choice, try again.")




