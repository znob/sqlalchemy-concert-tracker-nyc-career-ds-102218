from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from datetime import date
from base import Base
from user import User
from band import Band
from city import City
from show_song import ShowSong
from show import Show
from song import Song
from user_show import UserShow
from venue import Venue

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Users
person1 = User(name="John Doe")
person2 = User(name="Frank Stallone")
person3 = User(name="Grace Kelly")
session.add_all([person1, person2, person3])

# Shows
phirst_show = date(2003,11,28)
phish_11_28_03 = Show(date = phirst_show)

ph_1995 = date(1995, 12, 31)
phish_12_31_95 = Show(date = ph_1995)

cornell_77 = date(1977, 5, 8)
dead_5_8_77 = Show(date = cornell_77)

sunshine_daydream = date(1972, 8, 27)
dead_venetta = Show(date = sunshine_daydream)

dead_msg = date(1979, 1, 7)
dead_1_7_79 = Show(date = dead_msg)

# Bands
phish = Band(name='Phish')
dead = Band(name="Grateful Dead")
my_hs_garage_band = Band(name="My Band From High School")

phish.shows.extend([phish_12_31_95, phish_11_28_03])
dead.shows.extend([dead_5_8_77, dead_venetta, dead_1_7_79])
person1.shows.extend([dead_5_8_77, phish_12_31_95, phish_11_28_03])
person2.shows.extend([dead_venetta, dead_5_8_77])
person3.shows.append(dead_venetta)

# Cities
uniondale = City(name="Uniondale, NY")
veneta = City(name="Veneta, OR")
nyc = City(name="New York, NY")
ithaca = City(name="Ithaca, NY")

# Venues
nassau_coliseum = Venue(name='Nassau Veterans Memorial Coliseum', capacity=17686)
springfield_creamery = Venue(name='Springfield Creamery', capacity=30000)
msg = Venue(name="Madison Square Garden", capacity=20789)
barton_hall = Venue(name="Barton Hall", capacity=5000)
brooklyn_bowl = Venue(name="Brooklyn Bowl", capacity=600)

nassau_coliseum.city = uniondale
springfield_creamery.city = veneta
msg.city = nyc
barton_hall.city = ithaca
brooklyn_bowl.city = nyc

phish_11_28_03.venue = nassau_coliseum
phish_12_31_95.venue = msg
dead_5_8_77.venue = barton_hall
dead_venetta.venue = springfield_creamery
dead_1_7_79.venue = msg

# Songs
mikes = Song(name="Mike's Song")
brown_eyed_women = Song(name="Brown Eyed Women")
scarlet_begonias = Song(name="Scarlet Begonias")
fire = Song(name="Fire On the Mountain")

phish_11_28_03.songs.append(mikes)
phish_12_31_95.songs.append(mikes)
dead_5_8_77.songs.extend([brown_eyed_women, scarlet_begonias, fire])

cornell_scarlet = session.query(ShowSong).filter_by(id=4).one()
cornell_scarlet.length = 675
cornell_scarlet.notes = "famous Cornell Scarlet->Fire"

session.add_all([phish_11_28_03, phish_12_31_95, dead_5_8_77, dead_venetta, dead_1_7_79])
session.add_all([phish, dead, my_hs_garage_band])
session.add_all([uniondale, veneta, nyc, ithaca])
session.add_all([nassau_coliseum, springfield_creamery, msg, barton_hall])
session.add_all([mikes, brown_eyed_women, scarlet_begonias, fire])
session.add(cornell_scarlet)

session.commit()
