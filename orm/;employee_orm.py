# create the base class for our models
from sqlalchemy.orm import declarative_base  
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# step 1
engine = create_engine('sqlite:///company.db')
# step 2
Base = declarative_base()
# step 3
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)
# step 4
Base.metadata.create_all(engine)
# step 5
Session = sessionmaker(bind=engine)
session = Session()
e1 = Employee(name='Alice', age=30, department='HR')
e2 = Employee(name='Bob', age=25, department='IT')
session.add(e1)
session.add(e2)
session.commit()
*
# delete an employee
empp = session.query(Employee).filter_by(name='Alice').first()
if empp:
    session.delete(empp)
    session.commit()

# after deletion, update again to see the changes

emp = session.query(Employee).all()

for emp in emp:
    print(emp.name, emp.age, emp.department)
