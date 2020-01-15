from sqlalchemy import *
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///cot.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Incident(Base):
    __tablename__ = 'incident'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    latitude = Column(Numeric(15, 10))
    longitude = Column(Numeric(15, 10))

