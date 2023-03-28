from models import *
# from account_cli import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
    
Session=sessionmaker(bind=engine)
session = Session()

#USERS CREATED

users_list = [User(
        first_name='Kat',
        last_name='Dog',
        password='123',
    ),

User(
        first_name='James',
        last_name='Bond',
        password='casino',
    ),

User(
        first_name='Edd',
        last_name='Hi',
        password='butteredtoast',
    ),

User(
        first_name='Eddy',
        last_name='Bob',
        password='doubleD',
    ),

User(
        first_name='Josh',
        last_name='Hill',
        password='doubleD',
    ),

User(
    first_name='Nick',
    last_name='Brereton',
    password='doubleD'
),

User(
    first_name='Craig',
    last_name='Simpson',
    password='bart'
),

User(
    first_name='Eric',
    last_name='Cartmen',
    password='ass'
),

User(
    first_name='Clyde',
    last_name='Donovan',
    password='wendy'
),

User(
    first_name='Wendy',
    last_name='Strauss',
    password='pink'
),

User(
    first_name='Bebe',
    last_name='King',
    password='nice'
),

User(
    first_name='Julie',
    last_name='Julia',
    password='jules'
),

User(
    first_name='Bot',
    last_name='Dot',
    password='Rot'
),

User(
    first_name='Ronald',
    last_name='Raegan',
    password='america'
),

User(
    first_name='Gwen',
    last_name='Stefani',
    password='escape'
),

User(
    first_name='Tony',
    last_name='Soprano',
    password='gabagool'
),

User(
    first_name='Meadow',
    last_name='Soprano',
    password='jersey'
),

User(
    first_name='Christopher',
    last_name='K.',
    password='kh2'
),

User(
    first_name='Samurai',
    last_name='Jack',
    password='katana'
),

User(
    first_name='Beyonce',
    last_name='JayZ',
    password='blackalbum'
),

User(
    first_name='Barbara',
    last_name='Bush',
    password='cowboys'
),

User(
    first_name='Sally',
    last_name='Sullivan',
    password='pool'
),

User(
    first_name='Harold',
    last_name='Sephora',
    password='makeup'
),

User(
    first_name='Dusty',
    last_name='Taint',
    password='sand'
),

User(
    first_name='Orlando',
    last_name='Magic',
    password='bbal'
),

User(
    first_name='Jessica',
    last_name='Rabbit',
    password='carrots'
),

User(
    first_name='Nancy',
    last_name='Pelosi',
    password='crack'
)]




#USER ATTRIBUTES

attributes_list = [User_Attributes(
        interests='hotdogs, technology, money',
        age=34,
        height= 164,
        astrology = 'Scorpio',
        drinking = True,
        smoking = True,
        datingpref = 'polyamerous',
        passport = 'USA',
        user_id= 1,
    ),

User_Attributes(
        interests='cars, women, watches',
        age=43,
        height= 183,
        astrology = 'Taurus',
        drinking = True,
        smoking = True,
        datingpref = 'polyamerous',
        passport = 'United Kingdom',
        user_id= 2,
    ),

User_Attributes(
        interests='hotdogs, technology, money',
        age=20,
        height= 177,
        astrology = 'Gemini',
        drinking = True,
        smoking = False,
        datingpref = 'monogamous',
        passport = 'Canada',
        user_id= 3,
    ),

User_Attributes(
        interests='jawbreakers, clothes, women',
        age=18,
        height= 162,
        astrology = 'Virgo',
        drinking = False,
        smoking = True,
        datingpref = 'celibate',
        passport = 'Mongolia',
        user_id= 4,
    ),

User_Attributes(
        interests='paperplanes, rowing, tacos',
        age=67,
        height= 200,
        astrology = 'Aquarius',
        drinking = False,
        smoking = False,
        datingpref = 'polyamerous',
        passport = 'Netherlands',
        user_id= 5,
    ),

User_Attributes(
    interests = 'celsius, crying, zins',
    age=26,
    height=185,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    datingpref = 'Polyamerous',
    passport = 'USA',
    user_id = 6
),

User_Attributes(
    interests = 'soft things, crying, death metal',
    age=30,
    height=140,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Tanzania',
    user_id = 7
),

User_Attributes(
    interests = 'hurting people, cheetos, group therapy',
    age=21,
    height=166,
    astrology='Scorpio',
    drinking = True,
    smoking = True,
    datingpref = 'Polyamerous',
    passport = 'Thailand',
    user_id = 8
),

User_Attributes(
    interests = 'videogames, red wine, boats',
    age=29,
    height=171,
    astrology='Cancer',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Turkey',
    user_id = 9
),

User_Attributes(
    interests = 'wendys, ice skating, bubble baths',
    age=22,
    height=192,
    astrology='Leo',
    drinking = False,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'India',
    user_id = 10
),

User_Attributes(
    interests = 'tiktok, blues, donating blood',
    age=27,
    height=210,
    astrology='Virgo',
    drinking = False,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'USA',
    user_id = 11
),

User_Attributes(
    interests = 'chairs, botany, sneakers',
    age=37,
    height=173,
    astrology='Aries',
    drinking = True,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'Mexico',
    user_id = 12
),

User_Attributes(
    interests = 'robots, technology, death metal',
    age=31,
    height=188,
    astrology='Libra',
    drinking = False,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'Singapore',
    user_id = 13
),

User_Attributes(
    interests = 'politics, nuclear bombs, milkshakes',
    age=76,
    height=171,
    astrology='Libra',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Russia',
    user_id = 14
),

User_Attributes(
    interests = 'gabagool, warm bread, guns',
    age=59,
    height=190,
    astrology='Pisces',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Italy',
    user_id = 15
),

User_Attributes(
    interests = 'dolls, skydiving, surfing',
    age=21,
    height=162,
    astrology='Sagittarius',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'USA',
    user_id = 16
),

User_Attributes(
    interests = 'gold, beaches, pitbulls',
    age=38,
    height=159,
    astrology='Gemini',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Egypt',
    user_id = 17
),

User_Attributes(
    interests = 'gabagool, cheetos, boats',
    age=37,
    height=166,
    astrology='Scorpio',
    drinking = False,
    smoking = True,
    datingpref = 'polyamorous',
    passport = 'Kenya',
    user_id = 18
),

User_Attributes(
    interests = 'singing, beach, tanning',
    age=41,
    height=169,
    astrology='Pisces',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'South Korea',
    user_id = 19
),

User_Attributes(
    interests = 'football, red wine, money',
    age=37,
    height=163,
    astrology='Aries',
    drinking = True,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'Czechia',
    user_id = 20
),

User_Attributes(
    interests = 'salads, dogs, cleaning',
    age=29,
    height=155,
    astrology='Cancer',
    drinking = False,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'Poland',
    user_id = 21
),

User_Attributes(
    interests = 'makeup, drag shows, botany',
    age=44,
    height=179,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    datingpref = 'polyamerous',
    passport = 'Belgium',
    user_id = 22
),

User_Attributes(
    interests = 'cowboys, guns, money',
    age=66,
    height=163,
    astrology='Virgo',
    drinking = True,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'Vietnam',
    user_id = 23
),

User_Attributes(
    interests = 'basketball, wendys, money',
    age=29,
    height=181,
    astrology='Leo',
    drinking = True,
    smoking = True,
    datingpref = 'monogamous',
    passport = 'Bosnia',
    user_id = 24
),

User_Attributes(
    interests = 'carrots, snow, hurting people',
    age=26,
    height=160,
    astrology='Sagitarrius',
    drinking = False,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'North Korea',
    user_id = 25
),

User_Attributes(
    interests = 'politics, computers, death metal',
    age=71,
    height=170,
    astrology='Aries',
    drinking = False,
    smoking = False,
    datingpref = 'monogamous',
    passport = 'China',
    user_id = 26
)]



# USER LOCATION

location_list = [User_Location(
    zipcode=10002,
    location_pref=4,
    user_id = 1
),


User_Location(
    zipcode=10016,
    location_pref=18,
    user_id=3
),

User_Location(
    zipcode=10005,
    location_pref=12,
    user_id=4
),

User_Location(
    zipcode=10012,
    location_pref=14,
    user_id=5
),

User_Location(
    zipcode=10030,
    location_pref=15,
    user_id=6
),

User_Location(
    zipcode=10003,
    location_pref=1,
    user_id=7
),

User_Location(
    zipcode=11101,
    location_pref=20,
    user_id=8
),

User_Location(
    zipcode=11354,
    location_pref=20,
    user_id=9
),

User_Location(
    zipcode=11420,
    location_pref=20,
    user_id=10
),

User_Location(
    zipcode=11377,
    location_pref=20,
    user_id=11
),

User_Location(
    zipcode=11692,
    location_pref=20,
    user_id=12
),

User_Location(
    zipcode=11238,
    location_pref=20,
    user_id=13
),

User_Location(
    zipcode=11242,
    location_pref=20,
    user_id=14
),

User_Location(
    zipcode=11201,
    location_pref=7,
    user_id=15
),

User_Location(
    zipcode=11203,
    location_pref=4,
    user_id=16
),

User_Location(
    zipcode=11204,
    location_pref=5,
    user_id=17
),

User_Location(
    zipcode=10152,
    location_pref=9,
    user_id=18
),

User_Location(
    zipcode=10165,
    location_pref=5,
    user_id=19
),

User_Location(
    zipcode=10278,
    location_pref=3,
    user_id=20
),

User_Location(
    zipcode=10460,
    location_pref=11,
    user_id=21
),

User_Location(
    zipcode=10465,
    location_pref=2,
    user_id=22
),

User_Location(
    zipcode=10455,
    location_pref=15,
    user_id=23
),

User_Location(
    zipcode=11432,
    location_pref=5,
    user_id=24
),

User_Location(
    zipcode=11374,
    location_pref=8,
    user_id=25
),

User_Location(
    zipcode=11697,
    location_pref=9,
    user_id=26
),

User_Location(
    zipcode=10153,
    location_pref=2,
    user_id=27
)]
    
def delete_data():
    session.query(User).delete()
    session.query(User_Attributes).delete()
    session.query(User_Location).delete()
    session.query(Matches).delete()
    session.commit()

if __name__ == '__main__':
    delete_data()

    for user in users_list:
        existing_user = session.query(User).filter_by(first_name=user.first_name, last_name=user.last_name).first()
        if not existing_user:
            session.add(user)
    session.commit()

    for attribute in attributes_list:
        session.add(attribute)
    session.commit()

    for location in location_list:
        session.add(location)
    session.commit()

    # for match in matches_list:
    #     session.add(match)
    # session.commit()

# session.bulk_save_objects(users_list)
# session.bulk_save_objects(attributes_list)
# session.bulk_save_objects(location_list)
# session.commit()



