from connections import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, Integer, String


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    dead_line = Column(Date)
    description = Column(String)
    profile_id = Column(Integer, ForeignKey('profiles.id'))

    profile = relationship('Profile', back_populates='task')