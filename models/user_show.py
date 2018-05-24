from sqlalchemy import *
from base import Base

class UserShow(Base):
    __tablename__ = 'user_shows'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'), primary_key=True)
