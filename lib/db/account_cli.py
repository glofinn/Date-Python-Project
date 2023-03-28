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

#CREATE ACCOUNT FUNCTION
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

#LOGIN FUNCTION
def login(session, first_name, last_name, password):
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name, password=password).first()
    if user:
        print(f"Welcome, {first_name} {last_name}!")
    else:
        print("Invalid credentials. Please try again.")


#SET ATTRIBUTES FUNCTION
def set_attributes(session, first_name, last_name):
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        attributes = {
            "interests": input("Enter your interests (comma-separated): "),
            "age": int(input("Enter your age: ")),
            "height": float(input("Enter your height (in cm): ")),
            "astrological_sign": input("Enter your astrological sign: "),
            "drinking": input("Do you drink? (yes/no): ").lower() == "yes",
            "smoking": input("Do you smoke? (yes/no): ").lower() == "yes",
            "dating_preference": input("What type of relationship are you seeking? (e.g., friendship, dating, etc.): "),
        }

        for key, value in attributes.items():
            user_attribute = session.query(models.User_Attributes).filter(models.User_Attributes.user_id == user.id, models.User_Attributes.id == key).first()
            if user_attribute:
                user_attribute.value = value
            else:
                new_user_attribute = models.User_Attributes(user_id=user.id, key=key, value=value)
                session.add(new_user_attribute)

        session.commit()
        print(f"Attributes set for {first_name} {last_name}")
    else:
        print("User not found. Please create an account first.")


#DELETE ALL DATA FUNCTION
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

    set_attr_parser = subparsers.add_parser("set_attributes", help="Set user attributes")
    set_attr_parser.add_argument("first_name", type=str, help="First Name")
    set_attr_parser.add_argument("last_name", type=str, help="Last Name")

    args = parser.parse_args()

    if args.action == "create":
        create_account(session, args.first_name, args.last_name, args.password)
    elif args.action == "login":
        login(session, args.first_name, args.last_name, args.password)
    elif args.action == "set_attributes":
        set_attributes(session, args.first_name, args.last_name)
    else:
        print("Invalid command. Please use 'create', 'login', or 'set_attributes'.")

    # Set up the database connection and session
    

    # if args.action == "create":
    #     create_account(session, args.first_name, args.last_name, args.password)
    # elif args.action == "login":
    #     login(session, args.first_name, args.last_name, args.password)
    # else:
    #     parser.print_help()



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