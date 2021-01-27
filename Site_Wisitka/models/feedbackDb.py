from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from .meta import Base


class FeedbackDb(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    phone = Column(Text)


Index('my_index', FeedbackDb.username, unique=True, mysql_length=255)
