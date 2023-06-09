from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer, ForeignKey, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class User(Base):

    def __init__(self, first_name, last_name, password):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    logged_in = False
     

    attributes = relationship("User_Attributes", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, " + \
            f"FirstName={self.first_name}, " + \
            f"LastName={self.last_name},)"
    


class User_Attributes(Base):

    def __init__(self,interests,age,height,astrology,drinking,smoking,datingpref,passport,user_id):
        self.id= None
        self.interests=interests
        self.age=age
        self.height=height
        self.astrology=astrology
        self.drinking=drinking
        self.smoking=smoking
        self.datingpref=datingpref
        self.passport=passport
        self.user_id=user_id



    __tablename__ = 'user_attributes'
    id = Column(Integer, primary_key=True)
    interests = Column(String(), nullable=False)
    age = Column(Integer(), nullable=False)
    height = Column(Integer())
    astrology = Column(String(),)
    drinking = Column(Boolean(), default=False)
    smoking = Column(Boolean(), default=False)
    datingpref = Column(String(),)
    passport = Column(String(), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))


    user = relationship("User", back_populates="attributes")


    def __repr__(self):
        return f"Attributes(id={self.id}, " + \
            f"interests={self.interests}, " + \
            f"age={self.age}, " + \
            f"height={self.height}, " + \
            f"astrology={self.astrology}, " + \
            f"drinking={self.drinking}, " + \
            f"smoking={self.smoking}, " + \
            f"datingpref={self.datingpref}, " + \
            f"passport={self.passport}, " + \
            f"userID={self.user_id}, "
        
class User_Location(Base):

    def __init__(self, zipcode, location_pref, user_id):
        self.id = None
        self.zipcode = zipcode
        self.location_pref = location_pref
        self.user_id = user_id


    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    zipcode = Column(Integer(),)
    location_pref = Column(Integer(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


    def __repr__(self):
        return f"Location(id={self.id}, " + \
            f""
            
    

class Matches(Base):

    def __init__(self, user1, user2, date_matched, met, match_score, distance):
        self.id = None
        self.user1 = user1
        self.user2 = user2
        self.date_matched = date_matched
        self.met = met
        self.match_score = match_score
        self.distance = distance

    __tablename__ = 'matches'
    match_id = Column(Integer, primary_key=True)
    # user1=Column(Integer, ForeignKey('users.id'), nullable=False)
    # user2=Column(Integer, ForeignKey('users.id'), nullable=False)
    user1=Column(String, nullable=False)
    user2=Column(String, nullable=False)
    date_matched = Column(DateTime)
    met = Column(Boolean, default=False)
    match_score = Column(Integer, default=0)
    distance = Column(Integer)

    def __repr__(self):
        return f"Matches(match_id={self.match_id}, user1={self.user1}, user2={self.user2}, date_matched='{self.date_matched}', met={self.met})"
    

##FUNCTIONS

# def create_account(session, first_name, last_name, password):
#     user = User(first_name=first_name, last_name=last_name, password=password)
#     session.add(user)
#     session.commit()
#     print(f"Account created for {first_name} {last_name}")

# def login(session, first_name, last_name, password):
#     user = session.query(User).filter_by(first_name=first_name, last_name=last_name).first()
#     if user and user.password == password:
#         print(f"Welcome, {first_name} {last_name}!")
#     else:
#         print("Invalid credentials")


# if __name__ == '_main_':


#     parser = argparse.ArgumentParser(description="User management CLI")
#     subparsers = parser.add_subparsers(dest="command")

#     create_parser = subparsers.add_parser("create", help="Create a new user account")
#     create_parser.add_argument("first_name", help="User's first name")
#     create_parser.add_argument("last_name", help="User's last name")

#     login_parser = subparsers.add_parser("login", help="Log in to an existing user account")
#     login_parser.add_argument("first_name", help="User's first name")
#     login_parser.add_argument("last_name", help="User's last_name")

#     args = parser.parse_args()

#     if args.command == "create":
#         password = getpass("Enter a password: ")
#         confirm_password = getpass("Confirm password: ")
#         if password == confirm_password:
#             create_account(session, args.first_name, args.last_name, password)
#         else:
#             print("Passwords do not match. Account not created.")
#     elif args.command == "login":
#         password = getpass("Enter your password: ")
#         login(session, args.first_name, args.last_name, password)
#     else:
#         parser.print_help()









# finn = User('Finn', 'Chen', '123')

    
    

