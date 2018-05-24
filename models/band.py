from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship
from show import Show

class Band(Base):
    __tablename__ = "bands"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    shows = relationship('Show', order_by=Show.id, back_populates='band')
