from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

class LinkedInProfile(Base):
    """
    SQLAlchemy model for storing LinkedIn profile data in an SQLite database.
    Each profile is identified by its URL.
    """
    __tablename__ = 'linkedin_profiles'  # Define the table name
    url = Column(String, primary_key=True)  # LinkedIn profile URL
    about = Column(Text)  # About section
    experience = Column(Text)  # Experience section
    education = Column(Text)  # Education section

# Create a new SQLite database and table
engine = create_engine('sqlite:///linkedin_profiles.db')
Base.metadata.create_all(engine)  # Create tables based on the defined models

# Set up the session for database transactions
Session = sessionmaker(bind=engine)
session = Session()

def store_profile_data(url, profile_data):
    """
    Stores the scraped LinkedIn profile data into the SQLite database.
    """
    profile = LinkedInProfile(url=url, **profile_data)  # Create a new LinkedInProfile object
    session.add(profile)  # Add the profile to the session
    session.commit()  # Commit the transaction (save the profile)
