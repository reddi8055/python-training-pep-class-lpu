from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import asc, desc
# Database connection
engine = create_engine('sqlite:///inventory.db')
Base = declarative_base()
# Table Model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    def __repr__(self):
        return f"<Product(name={self.name}, category={self.category}, price={self.price}, stock={self.stock})>"
# Create table
Base.metadata.create_all(engine)
# Session setup
Session = sessionmaker(bind=engine)
session = Session()
#INSERT
p1 = Product(name="Laptop", category="Electronics", price=75000, stock=10)
p2 = Product(name="Headphones", category="Electronics", price=2000, stock=50)
p3 = Product(name="Coffee Mug", category="Home", price=300, stock=100)
p4 = Product(name="Office Chair", category="Furniture", price=8500, stock=5)
p5 = Product(name="Notebook", category="Stationery", price=50, stock=200)
session.add_all([p1, p2, p3, p4, p5])
session.commit()
print("\n--- All Products ---")
products = session.query(Product).all()
for p in products:
    print(p)
#UPDATE(Increase price where category is Electronics)
session.query(Product).filter(Product.category == "Electronics").update(
    {Product.price: Product.price * 1.10}
)
session.commit()
print("\n--- After Price Update ---")
for p in session.query(Product).all():
    print(p)
#DELETE(Remove products with low stock)
session.query(Product).filter(Product.stock < 10).delete()
session.commit()
print("\n--- After Deleting Low Stock Products ---")
for p in session.query(Product).all():
    print(p)
session.close()


print("\n--- Querying Products with Price > 5000 ---")
inv = session.query(Product).filter(Product.price > 5000).one_or_none()
if inv:
    print(inv)
else:
    print("No product found")

print ("\n after ascending order by price")
aes = session.query(Product).order_by(asc(Product.price)).all()
for p in aes:
    print(p)

print ("after applying limiting the results to 3")
limited = session.query(Product).order_by(asc(Product.price)).limit(3).all()
for p in limited:
    print(p)
