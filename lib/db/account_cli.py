from seed import session
import argparse
import models
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "sqlite:///users.db"
engine = create_engine(db_url)
models.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_account(session, first_name, last_name, password):
    # delete_data()
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()
    if user:
        print("User already exists in the database.")
    else:
        new_user = models.User(first_name=first_name, last_name=last_name, password=password)
        session.add(new_user)
        session.commit()
        print(f"Account created for {first_name} {last_name}")


def login(session, first_name, last_name, password):
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name, password=password).first()
    if user:
        print(f"Welcome, {first_name} {last_name}!")
    else:
        print("Invalid credentials. Please try again.")

def delete_data():
    session.query(User).delete()
    session.query(User_Attributes).delete()
    session.query(User_Location).delete()
    session.query(Matches).delete()
    session.commit()


if __name__ == "__main__":
    # delete_data()
    parser = argparse.ArgumentParser(description="User Account Creation and Login")
    subparsers = parser.add_subparsers(dest="action")

    create_parser = subparsers.add_parser("create", help="Create a new user account")
    create_parser.add_argument("first_name", type=str, help="First Name")
    create_parser.add_argument("last_name", type=str, help="Last Name")
    create_parser.add_argument("password", type=str, help="Password")

    login_parser = subparsers.add_parser("login", help="Login to an existing user account")
    login_parser.add_argument("first_name", type=str, help="First Name")
    login_parser.add_argument("last_name", type=str, help="Last Name")
    login_parser.add_argument("password", type=str, help="Password")

    args = parser.parse_args()

    # Set up the database connection and session
    

    if args.action == "create":
        create_account(session, args.first_name, args.last_name, args.password)
    elif args.action == "login":
        login(session, args.first_name, args.last_name, args.password)
    else:
        parser.print_help()



# def create_account(session, first_name, last_name, password):
#     user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name, password=password).first()
#     if user:
#         print("User already exists in the database.")
#     else:
#         new_user = models.User(first_name=first_name, last_name=last_name, password=password)
#         session.add(new_user)
#         session.commit()
#         print(f"Account created for {first_name} {last_name}")


# def create_account(session, first_name, last_name, password):
#     user = models.User(first_name=first_name, last_name=last_name, password=password)
#     session.add(user)
#     session.commit()
#     print(f"Account created for {first_name} {last_name}")
#     user_check = session.query(models.User).filter_by(first_name=first_name, last_name=last_name, password=password).first()
#     if user_check:
#         print("User successfully added to the database.")
#     else:
#         print("User not added to the database.")