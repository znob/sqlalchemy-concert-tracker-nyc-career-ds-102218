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

me = User(name="Jake MacNaughton")

phirst_show = date(2003,11,28)
phish_11_28_03 = Show(date = phirst_show)
phish = Band(name='Phish')

phish.shows.append(phish_11_28_03)
me.shows.append(phish_11_28_03)

uniondale = City(name="Uniondale, NY")
nassau_coliseum = Venue(name='Nassau Veterans Memorial Coliseum', capacity=17686)

nassau_coliseum.city = uniondale
phish_11_28_03.venue = nassau_coliseum

mikes = Song(name="Mike's Song")

phish_11_28_03.songs.append(mikes)

session.add(me)
session.add(phish_11_28_03)
session.add(uniondale)
session.add(nassau_coliseum)
session.add(mikes)

session.query(ShowSong).all()[0].length = 629
session.query(ShowSong).all()[0].notes = 'first ever mikes song attended'
import pdb; pdb.set_trace()
