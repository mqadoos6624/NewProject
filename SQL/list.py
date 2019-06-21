import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    data = db.execute("SELECT first_name,last_name,cnic FROM data")
    for value in data:
        print(f"{data.first_name} to {data.last_name} with {data.cnic} number")

if __name__ == "__main__":
    main()
