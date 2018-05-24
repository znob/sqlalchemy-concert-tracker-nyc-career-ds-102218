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

    # def total_shows(self):
    #
