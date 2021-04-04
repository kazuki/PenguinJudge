from contextlib import contextmanager
import os
from typing import TYPE_CHECKING, Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from penguin_judge import config

if TYPE_CHECKING:
    from sqlalchemy.orm.session import Session as BaseSession

Session = scoped_session(sessionmaker())
Session.configure(bind=create_engine(config.db_url.replace('+asyncpg', '')))

@contextmanager
def transaction() -> Iterator['BaseSession']:
    try:
        yield Session
        Session.commit()
    except Exception:
        Session.rollback()
        raise
    finally:
        Session.remove()
