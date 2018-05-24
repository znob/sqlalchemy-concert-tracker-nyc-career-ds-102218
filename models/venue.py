from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship
from show import Show

class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates="venues")
    name = Column(String)
    capacity = Column(Integer)
    shows = relationship('Show', order_by=Show.id, back_populates='venue')
