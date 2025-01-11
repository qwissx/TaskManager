from connections import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    profile_id = Column(Integer, ForeignKey('profiles.id'))

    profile = relationship('Profile', back_populates='user')