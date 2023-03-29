from seed import session
import argparse
import models
from models import *
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker


#CREATE ACCOUNT FUNCTION
def create_account(session, first_name, last_name, password):
    # delete_data()
    first_name = input('Please enter your first name:')
    last_name = input('Please enter your last name:')
    password = input('Please enter your password:')
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
    first_name = input('Please enter your first name:')
    last_name = input('Please enter your last name:')
    password = input('Please enter your password:')
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name, password=password).first()
    if user:
        user.logged_in = True
        print(f"Welcome, {first_name} {last_name} !")
        session.commit()
        return user

    else:
        print("Invalid credentials. Please try again.")
        return None

#SET ATTRIBUTES FUNCTION
def set_attributes(session, first_name, last_name):
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        interests = input("Enter your interests (comma-separated):")
        age = int(input("Enter your age: "))
        height = float(input("Enter your height (in cm): "))
        astrological_sign = input("Enter your astrological sign: ")
        drinking = input("Do you drink? (yes/no): ").lower() == "yes"
        smoking = input("Do you smoke? (yes/no): ").lower() == "yes"
        dating_preference = input("What type of relationship are you seeking? (e.g., friendship, dating, etc.): ")
        passport = input('What type of passport do you have:')
        user_id = user.id

        new_user_attribute = User_Attributes(interests, age, height, astrological_sign, drinking, smoking, dating_preference, passport, user_id)
        session.add(new_user_attribute)
        session.commit()

        print(f"Attributes set for {first_name} {last_name}")
    else:
        print("User not found. Please create an account first.")


def set_location(session, first_name, last_name):
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()

    if user:
        zipcode = int(input("Enter your zipcode:"))
        distancepref = int(input("Enter the max match distance(km): "))
        user_id = user.id

        new_location_pref = User_Location(zipcode, distancepref, user_id)
        session.add(new_location_pref)
        session.commit()

        print(f"Location Preferences set for {first_name} {last_name}")
    else:
        print("User not found. Please create an account first.")


#MATCHING FUNCTION
def match_me(session, first_name, last_name,):
    # Retrieve the user's attributes and user information
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()
    user_attributes = session.query(User_Attributes).filter_by(user_id=user.id).first()

    # Iterate through all other users' attributes and find matches
    for other_user_attributes in session.query(User_Attributes).join(models.User).filter(models.User.id != user.id):
        match_score = 0
        if user_attributes.interests == other_user_attributes.interests:
            match_score += 1
        if user_attributes.age == other_user_attributes.age:
            match_score += 1
        if abs(user_attributes.height - other_user_attributes.height) <= 5:
            match_score += 1
        if user_attributes.astrology == other_user_attributes.astrology:
            match_score += 1
        if user_attributes.drinking == other_user_attributes.drinking:
            match_score += 1
        if user_attributes.smoking == other_user_attributes.smoking:
            match_score += 1
        if user_attributes.datingpref == other_user_attributes.datingpref:
            match_score += 1
        if user_attributes.passport != other_user_attributes.passport:
            match_score += 1

        # Create a new match entry if there is a match
        if match_score >= 2:
            match = Matches(user1=user.first_name, user2=other_user_attributes.user.first_name, date_matched=datetime.now(), met=False, match_score=match_score)
            session.add(match)
            session.commit()
            print(f"Your match score is {match_score}!")

            # Adding the match to the other user's matches
            # other_user_match = Matches(user1=other_user_attributes.user.first_name, user2=user.first_name, date_matched=datetime.now(), met=False)
            # session.add(other_user_match)
            # session.commit()
            # print(f"Match added for {other_user_attributes.user.first_name}.")

    print("Matching complete.")

#DELETE ALL DATA FUNCTION
def delete_data():
    session.query(User).delete()
    session.query(User_Attributes).delete()
    session.query(User_Location).delete()
    session.query(Matches).delete()
    session.commit()


if __name__ == "__main__":

    db_url = "sqlite:///users.db"
    
    engine = create_engine(db_url)
    def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys = ON')
    event.listen(engine, 'connect', _fk_pragma_on_connect)
    #models.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

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

    set_location_parser = subparsers.add_parser("set_location", help="Set location")
    set_location_parser.add_argument("first_name", type=str, help="First Name")
    set_location_parser.add_argument("last_name", type=str, help="Last Name")

    match_me_parser = subparsers.add_parser("match_me", help="Find my matches!")
    match_me_parser.add_argument("first_name", type=str, help="First Name")
    match_me_parser.add_argument("last_name", type=str, help="Last Name")

    args = parser.parse_args()

    if args.action == "create":
        create_account(session, args.first_name, args.last_name, args.password)
    elif args.action == "login":
        login(session, args.first_name, args.last_name, args.password)
    elif args.action == "set_attributes":
        set_attributes(session, args.first_name, args.last_name)
    elif args.action == "set_location":
        set_location(session, args.first_name, args.last_name)
    elif args.action == "match_me":
        match_me(session, args.first_name, args.last_name)
    else:
        print("Invalid command. Please use 'create', 'login', 'set_attributes', 'set_location', or 'match_me.")

        # Prompt the user to log in or create an account

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