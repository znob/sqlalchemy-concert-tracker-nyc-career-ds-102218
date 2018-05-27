from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id  = Column(Integer, primary_key=True)
    name = Column(String)
    shows = relationship(
        'Show',
        secondary='user_shows'
    )

    def total_shows(self):
        return len(self.shows)

    def first_show(self):
        self.shows.sort(key=lambda show: show.date)
        first = self.shows[0]
        format_first = f"{first.band.name} - {first.date.strftime('%m/%d/%Y')} - {first.venue.name}, {first.venue.city.name}"
        return format_first
