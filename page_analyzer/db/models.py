from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(Date, nullable=False)
    checks = relationship("Urls_Checks", cascade="all, delete", 
                          passive_deletes=True)
    
    
class Urls_Checks(Base):
    __tablename__ = 'url_checks'
    id = Column(Integer, primary_key=True)
    url_id = Column(Integer, ForeignKey(Urls.id, ondelete='CASCADE'),
                    nullable=False)
    status_code = Column(Integer)
    h1 = Column(String)
    title = Column(String)
    description = Column(String)
    created_at = Column(Date, nullable=False)