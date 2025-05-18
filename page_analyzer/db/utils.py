from datetime import datetime
from typing import Optional

from sqlalchemy import desc

from page_analyzer.db.database import session_factory
from page_analyzer.db.models import Urls, Urls_Checks


def add_url(name: str):
    with session_factory() as session:
        url = Urls(
            name=name,
            created_at=datetime.now()
        )
        session.add(url)
        session.commit()
        
        
def get_url_by_id(id: int):
    with session_factory() as session:
        url = session.query(Urls).filter(Urls.id == id).first()
    return url


def get_url_by_name(name: str):
    with session_factory() as session:
        url = session.query(Urls).filter(Urls.name == name).first()
    return url


def get_all_urls():
    with session_factory() as session:
        urls = session.query(Urls).order_by(desc(Urls.id)).all()
    return urls

            
def detele_url(id: int):
    url = get_url_by_id(id)
    with session_factory() as session:
        session.delete(url)
        session.commit()
        
        
def add_url_check(url_id: int,
                  status_code: Optional[int] = None,
                  h1: Optional[str] = None,
                  title: Optional[str] = None,
                  description: Optional[str] = None):
    with session_factory() as session:
        url_check = Urls_Checks(
            url_id=url_id,
            status_code=status_code,
            h1=h1,
            title=title,
            description=description,
            created_at=datetime.now()
        )
        session.add(url_check)
        session.commit()
        
    
def get_last_url_check_by_id(id: int):
    with session_factory() as session:
        url_check = session.query(Urls_Checks). \
            filter(Urls_Checks.url_id == id). \
                order_by(desc(Urls_Checks.id)).first()
    return url_check


def get_url_check_by_url_id(id: int):
    with session_factory() as session:
        url_checks = session.query(Urls_Checks). \
            filter(Urls_Checks.url_id == id). \
                order_by(desc(Urls_Checks.id)).all()
    return url_checks