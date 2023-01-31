from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_tables(engine):
    Base.metadata.create_all(engine)

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    id_publisher = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship('Publisher', back_populates='books')

class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))
    count = Column(Integer)
    book = relationship('Book', back_populates='stocks')
    shop = relationship('Shop', back_populates='stocks')

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    date_sale = Column(Date)
    id_stock = Column(Integer, ForeignKey('stock.id'))
    count = Column(Integer)
    stock = relationship('Stock', back_populates='sales')

Publisher.books = relationship('Book', order_by=Book.id, back_populates='publisher')
Book.stocks = relationship('Stock', order_by=Stock.id, back_populates='book')
Shop.stocks = relationship('Stock', order_by=Stock.id, back_populates='shop')
Stock.sales = relationship('Sale', order_by=Sale.id, back_populates='stock')