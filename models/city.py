from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship
from venue import Venue

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    venues = relationship('Venue', order_by=Venue.id, back_populates='city')
