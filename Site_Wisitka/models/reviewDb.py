from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class ReviewDb(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    comment = Column(Text)
    date = Column(Text)


Index('my_index', ReviewDb.username, unique=True, mysql_length=255)
