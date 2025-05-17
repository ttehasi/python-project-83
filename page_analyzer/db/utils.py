from datetime import datetime

from sqlalchemy import desc

from page_analyzer.db.database import session_factory
from page_analyzer.db.models import Urls


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