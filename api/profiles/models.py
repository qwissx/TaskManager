from connections import Base
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Float)

    user = relationship('User', back_populates='profile')
    task = relationship('Task', back_populates='profile')