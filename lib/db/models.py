from sqlalchemy import PrimaryKeyConstraint, Column, String, Integer, ForeignKey, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base



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
    drinking = Column(Boolean(), default=False)
    smoking = Column(Boolean(), default=False)
    relationship = Column(String(),)
    passport = Column(String(), nullable=False)
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
            f"passport={self.passport}, " + \
            f"userID={self.user_id}, "
        
class User_Location(Base):

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    zipcode = Column(Integer(),)
    location_pref = Column(Integer(), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


    def __repr__(self):
        return f"Location(id={self.id}, " + \
            f""
            
    

class Matches(Base):

    __tablename__ = 'matches'
    match_id = Column(Integer, primary_key=True)
    user1=Column(Integer())
    user2=Column(Integer())
    date_matched = Column(DateTime, default=datetime.now())
    Met = Column(Boolean, default=False)

    def __repr__(self):
        return f"Matches"
    

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

    
    

