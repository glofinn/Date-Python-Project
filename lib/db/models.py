from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    def __init__(self, first_name, last_name, password):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        pass


    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    password = Column(String(), nullable=False) 

    def __repr__(self):
        return f"User(id={self.id}, " + \
            f"FirstName={self.first_name}, " + \
            f"LastName={self.last_name},)"
    


class User_Attributes(Base):



    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    interests = Column(String(), nullable=False)
    age = Column(Integer(), nullable=False)
    height = Column(Integer())
    astrology = Column(String(),)
    drinking = Column()
    smoking = Column()
    relationship = Column(String(),)
    user_id = Column(Integer(), ForeignKey('users.id'))

    def __repr__(self):
        return f"Attributes(id={self.id}, " + \
            f"interests={self.interests}, " + \
            f"age={self.age}, " + \
            f"height={self.height}, " + \
            f"astrology={self.astrology}, " + \
            f"drinking={self.drinking}, " + \
            f"smoking={self.smoking}, " + \
            f"relationship={self.relationship}, " + \
            f"userID={self.user_id}, "
        
class User_Location(Base):

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    borough = Column(String(), nullable=False)

    def __repr__(self):
        return f"Location(id={self.id}, " + \
            f"borough={self.borough}, "
    






    
    

