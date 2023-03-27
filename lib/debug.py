from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, User, User_Attributes, User_Location)

if __name__ == '__main__':
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)
    
    Session=sessionmaker(bind=engine)
    session = Session()
