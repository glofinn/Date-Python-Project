from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
    
Session=sessionmaker(bind=engine)
session = Session()

#USERS CREATED
kat = User(
        first_name='Kat',
        last_name='Dog',
        password='123',
    )

jamesbond=User(
        first_name='James',
        last_name='Bond',
        password='casino',
    )

edd=User(
        first_name='Edd',
        last_name='Hi',
        password='butteredtoast',
    )

eddy=User(
        first_name='Eddy',
        last_name='Bob',
        password='doubleD',
    )

josh=User(
        first_name='Josh',
        last_name='Hill',
        password='doubleD',
    )

nick = User(
    first_name='Nick',
    last_name='Brereton',
    password='doubleD'
)

craig = User(
    first_name='Craig',
    last_name='Simpson',
    password='bart'
)

eric = User(
    first_name='Eric',
    last_name='Cartmen',
    password='ass'
)

clyde = User(
    first_name='Clyde',
    last_name='Donovan',
    password='wendy'
)

wendy = User(
    first_name='Wendy',
    last_name='Strauss',
    password='pink'
)

bebe = User(
    first_name='Bebe',
    last_name='King',
    password='nice'
)

julie = User(
    first_name='Julie',
    last_name='Julia',
    password='jules'
)

bot = User(
    first_name='Bot',
    last_name='Dot',
    password='Rot'
)

ronald = User(
    first_name='Ronald',
    last_name='Raegan',
    password='america'
)

gwen = User(
    first_name='Gwen',
    last_name='Stefani',
    password='escape'
)

tony = User(
    first_name='Tony',
    last_name='Soprano',
    password='gabagool'
)

meadow = User(
    first_name='Meadow',
    last_name='Soprano',
    password='jersey'
)

christopher = User(
    first_name='Christopher',
    last_name='K.',
    password='kh2'
)

jack = User(
    first_name='Samurai',
    last_name='Jack',
    password='katana'
)

beyonce = User(
    first_name='Beyonce',
    last_name='JayZ',
    password='blackalbum'
)

barbara = User(
    first_name='Barbara',
    last_name='Bush',
    password='cowboys'
)

sally = User(
    first_name='Sally',
    last_name='Sullivan',
    password='pool'
)

harold = User(
    first_name='Harold',
    last_name='Sephora',
    password='makeup'
)

dusty = User(
    first_name='Dusty',
    last_name='Taint',
    password='sand'
)

orlando = User(
    first_name='Orlando',
    last_name='Magic',
    password='bbal'
)

jessica = User(
    first_name='Jessica',
    last_name='Rabbit',
    password='carrots'
)

nancy = User(
    first_name='Nancy',
    last_name='Pelosi',
    password='crack'
)




#USER ATTRIBUTES

kat_attributes = User_Attributes(
        interests='hotdogs, technology, money',
        age=34,
        height= 164,
        astrology = 'Scorpio',
        drinking = True,
        smoking = True,
        relationship = 'polyamerous',
        passport = 'USA',
        user_id= 1,
    )

jamesbond_attributes = User_Attributes(
        interests='cars, women, watches',
        age=43,
        height= 183,
        astrology = 'Taurus',
        drinking = True,
        smoking = True,
        relationship = 'polyamerous',
        passport = 'United Kingdom',
        user_id= 3,
    )

edd_attributes = User_Attributes(
        interests='hotdogs, technology, money',
        age=20,
        height= 177,
        astrology = 'Gemini',
        drinking = True,
        smoking = False,
        relationship = 'monogamous',
        passport = 'Canada',
        user_id= 4,
    )

eddy_attributes = User_Attributes(
        interests='jawbreakers, clothes, women',
        age=18,
        height= 162,
        astrology = 'Virgo',
        drinking = False,
        smoking = True,
        relationship = 'celibate',
        passport = 'Mongolia',
        user_id= 5,
    )

josh_attributes = User_Attributes(
        interests='paperplanes, rowing, tacos',
        age=67,
        height= 200,
        astrology = 'Aquarius',
        drinking = False,
        smoking = False,
        relationship = 'polyamerous',
        passport = 'Netherlands',
        user_id= 6,
    )

nick_attributes = User_Attributes(
    interests = 'celsius, crying, zins',
    age=26,
    height=185,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    relationship = 'Polyamerous',
    passport = 'USA',
    user_id = 7
)

craig_attributes = User_Attributes(
    interests = 'soft things, crying, death metal',
    age=30,
    height=140,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Tanzania',
    user_id = 8
)

eric_attributes = User_Attributes(
    interests = 'hurting people, cheetos, group therapy',
    age=21,
    height=166,
    astrology='Scorpio',
    drinking = True,
    smoking = True,
    relationship = 'Polyamerous',
    passport = 'Thailand',
    user_id = 9
)

clyde_attributes = User_Attributes(
    interests = 'videogames, red wine, boats',
    age=29,
    height=171,
    astrology='Cancer',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Turkey',
    user_id = 10
)

wendy_attributes = User_Attributes(
    interests = 'wendys, ice skating, bubble baths',
    age=22,
    height=192,
    astrology='Leo',
    drinking = False,
    smoking = True,
    relationship = 'monogamous',
    passport = 'India',
    user_id = 11
)

bebe_attributes = User_Attributes(
    interests = 'tiktok, blues, donating blood',
    age=27,
    height=210,
    astrology='Virgo',
    drinking = False,
    smoking = False,
    relationship = 'monogamous',
    passport = 'USA',
    user_id = 12
)

julie_attributes = User_Attributes(
    interests = 'chairs, botany, sneakers',
    age=37,
    height=173,
    astrology='Aries',
    drinking = True,
    smoking = False,
    relationship = 'monogamous',
    passport = 'Mexico',
    user_id = 13
)

bot_attributes = User_Attributes(
    interests = 'robots, technology, death metal',
    age=31,
    height=188,
    astrology='Libra',
    drinking = False,
    smoking = False,
    relationship = 'monogamous',
    passport = 'Singapore',
    user_id = 14
)

ronald = User_Attributes(
    interests = 'politics, nuclear bombs, milkshakes',
    age=76,
    height=171,
    astrology='Libra',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Russia',
    user_id = 15
)

tony_attributes = User_Attributes(
    interests = 'gabagool, warm bread, guns',
    age=59,
    height=190,
    astrology='Pisces',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Italy',
    user_id = 16
)

meadow_attributes = User_Attributes(
    interests = 'dolls, skydiving, surfing',
    age=21,
    height=162,
    astrology='Sagittarius',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'USA',
    user_id = 17
)

christopher_attributes = User_Attributes(
    interests = 'gold, beaches, pitbulls',
    age=38,
    height=159,
    astrology='Gemini',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Egypt',
    user_id = 18
)

jack_attributes = User_Attributes(
    interests = 'gabagool, cheetos, boats',
    age=37,
    height=166,
    astrology='Scorpio',
    drinking = False,
    smoking = True,
    relationship = 'polyamorous',
    passport = 'Kenya',
    user_id = 19
)

beyonce_attributes = User_Attributes(
    interests = 'singing, beach, tanning',
    age=41,
    height=169,
    astrology='Pisces',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'South Korea',
    user_id = 20
)

barbara_attributes = User_Attributes(
    interests = 'football, red wine, money',
    age=37,
    height=163,
    astrology='Aries',
    drinking = True,
    smoking = False,
    relationship = 'monogamous',
    passport = 'Czechia',
    user_id = 21
)

sally_attributes = User_Attributes(
    interests = 'salads, dogs, cleaning',
    age=29,
    height=155,
    astrology='Cancer',
    drinking = False,
    smoking = False,
    relationship = 'monogamous',
    passport = 'Poland',
    user_id = 22
)

harold_attributes = User_Attributes(
    interests = 'makeup, drag shows, botany',
    age=44,
    height=179,
    astrology='Capricorn',
    drinking = True,
    smoking = True,
    relationship = 'polyamerous',
    passport = 'Belgium',
    user_id = 23
)

dusty_attributes = User_Attributes(
    interests = 'cowboys, guns, money',
    age=66,
    height=163,
    astrology='Virgo',
    drinking = True,
    smoking = False,
    relationship = 'monogamous',
    passport = 'Vietnam',
    user_id = 24
)

orlando_attributes = User_Attributes(
    interests = 'basketball, wendys, money',
    age=29,
    height=181,
    astrology='Leo',
    drinking = True,
    smoking = True,
    relationship = 'monogamous',
    passport = 'Bosnia',
    user_id = 25
)

jessica_attributes = User_Attributes(
    interests = 'carrots, snow, hurting people',
    age=26,
    height=160,
    astrology='Sagitarrius',
    drinking = False,
    smoking = False,
    relationship = 'monogamous',
    passport = 'North Korea',
    user_id = 26
)

nancy_attributes = User_Attributes(
    interests = 'politics, computers, death metal',
    age=71,
    height=170,
    astrology='Aries',
    drinking = False,
    smoking = False,
    relationship = 'monogamous',
    passport = 'China',
    user_id = 27
)



# USER LOCATION

kat_location = User_Location(
    zipcode=10002,
    location_pref=4,
    user_id = 1
)


jamesbond_location = User_Location(
    zipcode=10016,
    location_pref=18,
    user_id=3
)

edd_location = User_Location(
    zipcode=10005,
    location_pref=12,
    user_id=4
)

eddy_location = User_Location(
    zipcode=10012,
    location_pref=14,
    user_id=5
)

josh_location = User_Location(
    zipcode=10030,
    location_pref=15,
    user_id=6
)

nick_location = User_Location(
    zipcode=10003,
    location_pref=1,
    user_id=7
)

craig_location = User_Location(
    zipcode=11101,
    location_pref=20,
    user_id=8
)

eric_location = User_Location(
    zipcode=11354,
    location_pref=20,
    user_id=9
)

clyde_location = User_Location(
    zipcode=11420,
    location_pref=20,
    user_id=10
)

wendy_location = User_Location(
    zipcode=11377,
    location_pref=20,
    user_id=11
)

bebe_location = User_Location(
    zipcode=11692,
    location_pref=20,
    user_id=12
)

julie_location = User_Location(
    zipcode=11238,
    location_pref=20,
    user_id=13
)

bot_location = User_Location(
    zipcode=11242,
    location_pref=20,
    user_id=14
)

ronald_location = User_Location(
    zipcode=11201,
    location_pref=7,
    user_id=15
)

tony_location = User_Location(
    zipcode=11203,
    location_pref=4,
    user_id=16
)

meadow_location = User_Location(
    zipcode=11204,
    location_pref=5,
    user_id=17
)

christopher_location = User_Location(
    zipcode=10152,
    location_pref=9,
    user_id=18
)

jack_location = User_Location(
    zipcode=10165,
    location_pref=5,
    user_id=19
)

beyonce_location = User_Location(
    zipcode=10278,
    location_pref=3,
    user_id=20
)

barbara_location = User_Location(
    zipcode=10460,
    location_pref=11,
    user_id=21
)

sally_location = User_Location(
    zipcode=10465,
    location_pref=2,
    user_id=22
)

harold_location = User_Location(
    zipcode=10455,
    location_pref=15,
    user_id=23
)

dusty_location = User_Location(
    zipcode=11432,
    location_pref=5,
    user_id=24
)

orlando_location = User_Location(
    zipcode=11374,
    location_pref=8,
    user_id=25
)

jessica_location = User_Location(
    zipcode=11697,
    location_pref=9,
    user_id=26
)

nancy_location = User_Location(
    zipcode=10153,
    location_pref=2,
    user_id=27
)
    
def delete_data():
    session.query(User).delete()
    session.query(User_Attributes).delete()
    session.query(User_Location).delete()
    session.query(Matches).delete()
    session.commit()

if __name__ == '__main__':
    delete_data()

session.bulk_save_objects([kat, jamesbond, edd, eddy, josh, nick])
session.bulk_save_objects([kat_attributes, jamesbond_attributes, edd_attributes, eddy_attributes, josh_attributes, nick_attributes])
session.bulk_save_objects([kat_location, nick_location])
session.commit()



