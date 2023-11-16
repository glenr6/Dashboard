from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    tokens = relationship('Token', back_populates='owner')

# Define the Token model
class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    last_updated = Column(DateTime, default=datetime.utcnow)
    price = Column(Float)
    volume = Column(Float)

    # Relationships
    owner = relationship('User', back_populates='tokens')

# Create the engine to connect to the database
engine = create_engine('sqlite:///crypto_dashboard.db')
Session = sessionmaker(bind=engine)

# Create all tables in the engine
Base.metadata.create_all(engine)


# TODO: modify models to fit specific Class data requirements 