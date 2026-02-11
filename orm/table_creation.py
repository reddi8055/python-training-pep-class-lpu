#import declarative_base to create a base class for our models.
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# STEP 1
engine=create_engine('sqlite:////school.db')
#create a base class for our models.
# STEP 2
Base=declarative_base()
#base will be parent class for all our models and will contain the metadata for our tables.
# STEP 3
class Student(Base):
    __tablename__='students' 
    id=Column(Integer, primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String)
# CREATE ALL TABLES DEFINED BY THE BASE CLASS
# STEP 4
Base.metadata.create_all(engine) #create the tables in the database.

# STEP 5
Session = sessionmaker(bind=engine) #create a session factory and bind it to the engine.
session = Session()
s1=Student(id=1,name='Rahul', age=20, course='Python')
s2=Student(id=2,name='Bob', age=22, course='Java')
s3=Student(id=3,name='Charlie', age=21, course='History')   
s4=Student(id=4,name='David', age=23, course='Math')
s5=Student(id=5,name='Eve', age=25, course='Science')
session.add(s1)
session.add(s2)
session.add(s3)
session.add(s4)
session.add(s5)
session.commit()
# session.add_all([s1,s2,s3,s4,s5]) #add the student objects to the session.
students = session.query(Student).all() #query all students from the database. UPDATE
for student in students:
    print(student.id, student.name, student.age, student.course)
print("Students added to the session.")

