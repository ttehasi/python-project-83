import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
from sqlalchemy.orm import sessionmaker

from page_analyzer.db.models import Base

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL').replace('postgres://', 'postgresql://')
registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')
engine = create_engine(DATABASE_URL)
session_factory = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)