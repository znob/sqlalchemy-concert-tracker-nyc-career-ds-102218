from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship, backref
from show import Show
from song import Song

class ShowSong(Base):
    __tablename__ = "show_songs"
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    song_id = Column(Integer, ForeignKey('songs.id'))
    length = Column(Integer)
    notes = Column(Text)
    show = relationship(Show, backref=backref("show_songs", cascade="all, delete-orphan"))
    song = relationship(Song, backref=backref("show_songs", cascade="all, delete-orphan"))
