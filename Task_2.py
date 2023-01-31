from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from Task_1 import Book, Sale, Shop, Stock, Publisher

# Connect to the database
engine = create_engine('postgresql://postgres:home_pc@127.0.0.1:5432/homework_ORM')
Session = sessionmaker(bind=engine)
session = Session()

# Get publisher name or id
publisher = input("Enter publisher name or id: ")

# Get purchases for the specified publisher
purchases = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
    select_from(Book).\
    join(Stock, Book.id == Stock.id_book).\
    join(Shop, Stock.id_shop == Shop.id).\
    filter(Publisher.name == publisher)

# Display the results
for purchase in purchases:
    print("{} | {} | {} | {}".format(purchase[0], purchase[1], purchase[2], purchase[3]))