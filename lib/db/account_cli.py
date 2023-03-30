from seed import session
import argparse
import models
from models import *
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from geopy.distance import geodesic
from uszipcode import SearchEngine
from datetime import datetime
import pgeocode




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
        user.logged_in = True
        print(f"Welcome, {first_name} {last_name} to Green Card Dating!")
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
        drinking = input("Do you drink? (if sometimes enter yes) (yes/no): ").lower() == "yes"
        smoking = input("Do you smoke? (if sometimes enter yes) (yes/no): ").lower() == "yes"
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
        print("User not found. Please enter correct credentials or create an account.")

##VIEW MATCHES FUNCTION
def view_matches(session, first_name, last_name):
    # Retrieve the user's matches
    matches = session.query(Matches).filter_by(user1=first_name, user2=last_name).all()
    if not matches:
        print("You don't have any matches yet.")
        return

    # Display the matches
    print("Here are your matches:")
    for match in matches:
        print(f"{match.user2} (match score: {match.match_score}, distance: {match.distance})")

    return

#MATCHING FUNCTION
def match_me(session, first_name, last_name):
    # Retrieve the user's attributes and user information
    user = session.query(models.User).filter_by(first_name=first_name, last_name=last_name).first()
    if user is None:
        print(f"User {first_name} {last_name} does not exist.")
        return

    user_attributes = session.query(User_Attributes).filter_by(user_id=user.id).first()
    user_location = session.query(models.User_Location).filter_by(user_id=user.id).first()

    search = SearchEngine()

    # Iterate through all other users' attributes and find matches
    for other_user_attributes in session.query(User_Attributes).join(models.User).filter(models.User.id != user.id):
        match_score = 0
        ##Split()?
        if user_attributes.interests == other_user_attributes.interests:
            match_score += 1
        if abs(user_attributes.age - other_user_attributes.age) <= 8:
            match_score += 1
        if abs(user_attributes.height - other_user_attributes.height) <= 5:
            match_score += 1
        if user_attributes.astrology != other_user_attributes.astrology:
            match_score += 1
        if user_attributes.drinking == other_user_attributes.drinking:
            match_score += 1
        if user_attributes.smoking == other_user_attributes.smoking:
            match_score += 1
        if user_attributes.datingpref == other_user_attributes.datingpref:
            match_score += 1
        if user_attributes.passport != other_user_attributes.passport:
            match_score += 1

        # Calculate distance and add score if it's within the user's location preference
        other_user_location = session.query(User_Location).filter_by(user_id=other_user_attributes.user_id).first()
        if user_location and other_user_location:
            user_zip = user_location.zipcode
            other_user_zip = other_user_location.zipcode
            user_lat, user_lon = search.by_zipcode(user_zip).lat, search.by_zipcode(user_zip).lng
            other_user_lat, other_user_lon = search.by_zipcode(other_user_zip).lat, search.by_zipcode(other_user_zip).lng
            distance = geodesic((user_lat, user_lon), (other_user_lat, other_user_lon)).kilometers
            # distance = pgeocode.GeoDistance('us')
            if distance <= user_location.location_pref:
                match_score += 1
            elif distance >= user_location.location_pref:
                match_score -= 1

        # Create a new match entry if there is a match
        if match_score >= 4:
            date_matched = datetime.now()
            match = Matches(user1=user.first_name, 
                            user2=other_user_attributes.user.first_name, 
                            date_matched=date_matched, 
                            met=False, 
                            match_score=match_score, 
                            distance=f"{round(distance,2)} kilometers")
            session.add(match)
            session.commit()
            print(f"Your match score with {other_user_attributes.user.first_name} is {match_score}!")

    print("Matching complete.")
    print("Please view your match table :)!")



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
create_parser.add_argument("--first-name", type=str, help="First Name")
create_parser.add_argument("--last-name", type=str, help="Last Name")
create_parser.add_argument("--password", type=str, help="Password")

login_parser = subparsers.add_parser("login", help="Login to an existing user account")
login_parser.add_argument("--first-name", type=str, help="First Name")
login_parser.add_argument("--last-name", type=str, help="Last Name")
login_parser.add_argument("--password", type=str, help="Password")

set_attr_parser = subparsers.add_parser("set_attributes", help="Set user attributes")
set_attr_parser.add_argument("--first_name", type=str, help="First Name")
set_attr_parser.add_argument("--last_name", type=str, help="Last Name")

set_location_parser = subparsers.add_parser("set_location", help="Set location")
set_location_parser.add_argument("--first_name", type=str, help="First Name")
set_location_parser.add_argument("--last_name", type=str, help="Last Name")

match_me_parser = subparsers.add_parser("match_me", help="Find my matches!")
match_me_parser.add_argument("--first_name", type=str, help="First Name")
match_me_parser.add_argument("--last_name", type=str, help="Last Name")

args = parser.parse_args()

if args.action == "create" or args.action == "login":
    if not args.first_name:
        args.first_name = input("Enter your first name: ")
    if not args.last_name:
        args.last_name = input("Enter your last name: ")
    if not args.password:
        args.password = input("Enter your password: ")
    if args.action == "create":
        create_account(session, args.first_name, args.last_name, args.password)
    if args.action == "login":
        login(session, args.first_name, args.last_name, args.password)

elif args.action == "set_attributes":
    if not args.first_name:
        args.first_name = input("Enter your first name: ")
    if not args.last_name:
        args.last_name = input("Enter your last name: ")
    if args.action == "set_attributes":
        set_attributes(session, args.first_name, args.last_name)
if args.action == "set_location":
    if not args.first_name:
        args.first_name = input("Enter your first name: ")
    if not args.last_name:
        args.last_name = input("Enter your last name: ")
    if args.action == "set_location":
        set_location(session, args.first_name, args.last_name)
elif args.action == "match_me":
        if not args.first_name:
            args.first_name = input("Enter your first name: ")
        if not args.last_name:
            args.last_name = input("Enter your last name: ")
        match_me(session, args.first_name, args.last_name)

    
    

# elif args.action == "set_location":
#     set_location(session, args.first_name, args.last_name)
# elif args.action == "match_me":
#     match_me(session, args.first_name, args.last_name)

    # parser = argparse.ArgumentParser(description="User Account Creation and Login")
    # subparsers = parser.add_subparsers(dest="action")

    
    # create_parser = subparsers.add_parser("create", help="Create a new user account")
    # create_parser.add_argument("first_name", type=str, help="First Name")
    # create_parser.add_argument("last_name", type=str, help="Last Name")
    # create_parser.add_argument("password", type=str, help="Password")

    # login_parser = subparsers.add_parser("login", help="Login to an existing user account")
    # login_parser.add_argument("first_name", type=str, help="First Name")
    # login_parser.add_argument("last_name", type=str, help="Last Name")
    # login_parser.add_argument("password", type=str, help="Password")

    # set_attr_parser = subparsers.add_parser("set_attributes", help="Set user attributes")
    # set_attr_parser.add_argument("first_name", type=str, help="First Name")
    # set_attr_parser.add_argument("last_name", type=str, help="Last Name")

    # set_location_parser = subparsers.add_parser("set_location", help="Set location")
    # set_location_parser.add_argument("first_name", type=str, help="First Name")
    # set_location_parser.add_argument("last_name", type=str, help="Last Name")

    # match_me_parser = subparsers.add_parser("match_me", help="Find my matches!")
    # match_me_parser.add_argument("first_name", type=str, help="First Name")
    # match_me_parser.add_argument("last_name", type=str, help="Last Name")



    # args = parser.parse_args()

    # if args.action == "create":
    #     create_account(session, args.first_name, args.last_name, args.password)
    #     # create_account(session)
    # elif args.action == "login":
    #     login(session, args.first_name, args.last_name, args.password)
    # elif args.action == "set_attributes":
    #     set_attributes(session, args.first_name, args.last_name)
    # elif args.action == "set_location":
    #     set_location(session, args.first_name, args.last_name)
    # elif args.action == "match_me":
    #     match_me(session, args.first_name, args.last_name)
    # else:
    #     print("Invalid command. Please use 'create', 'login', 'set_attributes', 'set_location', or 'match_me.")

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