# import create_engine to connect to the database 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///school.db')
#sql lite database
# file name is school.db
# will be created in the current directory if it does not exist
print("Connection done")
